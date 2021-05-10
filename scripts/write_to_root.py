import ROOT
import re
import os
from array import array
from dataclasses import dataclass
from collections import defaultdict
from itertools import chain
from functools import singledispatchmethod
from typing import Tuple
from argparse import ArgumentParser

parser = ArgumentParser()



@dataclass
class Token:
    kind: str
    value: str
    
@dataclass
class Filenames:
    filename_from: str
    filename_to: str
    
@dataclass
class Runs:
    run_from: int
    run_to: int

class Tokenizer(object):
    
    groups = (
        ('CLASS', r'\[\w+\]'),
        ('PARAMS', r'[^\[\]]*')
    )
    regex = re.compile(
        pattern='|'.join(f'(?P<{group[0]}>{group[1]})' for group in groups),
        flags=re.M
    )
    
    def __init__(self, text):
        self.text = text
    
    def __iter__(self):
        for match in self.regex.finditer(self.text.strip()):
            kind = match.lastgroup
            value = match.group()
            yield Token(
                kind=kind.strip(), 
                value=value.strip()
            )
  
            
class Converter(object):
    
    def __init__(self):
        self.table2params = defaultdict(lambda: '')
    
    def __setitem__(self, table_name, params):
        self.table2params[table_name] += params
    
    def __getitem__(self, table_name):
        return self.table2params[table_name]
    
    def save(self):
        output_file = ROOT.TFile('tree.root', 'recreate')
        output_tree = ROOT.TTree('T', 'Configurations/')
        leaf_list = ':'.join(table for table in self.table2params.keys())
        max_len = len(max(self.table2params.values(), key=len))
        s = '\n'.join(f'char {t}[] = "{str.encode(v)}";' for t, v in self.table2params.items()) +\
            '\nclass ConfStruct: public TObject{ \n' +\
            '\npublic: ' +\
            '\nConfStruct() {};' +\
            '\n~ConfStruct() {};' +\
            '\nClassDef(ConfStruct, 1)' +\
            '\n'.join(f'   char {t}[{max_len}];' for t in  self.table2params.keys()) +\
            '};\n' +\
            'ConfStruct * s = new ConfStruct();\n' +\
            'int i;\n' +\
            '\n'.join(f'for(i = 0; i<{len(v)};i++)' + ' '+ f's->{t}[i] = {t}[i+2]; ' + '\n' for t, v in self.table2params.items()) + \
            '''
            TFile *f = new TFile("tree.root","RECREATE");
            TTree *tree = new TTree("T","A Root Tree");
            tree->Branch("ConfBranch","ConfStruct",&s,32000,0);
            tree->Fill();
            tree->Write();
            tree->Print();
            f->Write();
            f->Close();
            
            f = new TFile("tree.root");
            t = (TTree*)f->Get("T");
            ConfStruct *event = 0;
            TBranch *conf = t->GetBranch("ConfBranch");
            conf->SetAddress(&event);
            ''' + \
            f'\nchar param[{max_len}]; ' +\
            f'\nfor(i=0;i<{max_len};i++) param[i] = (char)(event->SFibersStackDDUnpackerPar)[i];' +\
            '''
            //#include<iostream>
            //for (i=0; i<200; i++){
            //    std::cout << (char)param[i];
            //}
            '''
        print(s) 
        ROOT.gInterpreter.ProcessLine(s)
        
            
    
def write_to_root(conf_file_path):
    with open(conf_file_path) as file:
        tokenizer = Tokenizer(file.read())
        converter = Converter()
        current_table = None
        for token in tokenizer:
            if token.kind == 'CLASS':
                current_table = token.value[
                    token.value.index('[') + 1 : token.value.index(']')
                ]
            
            elif token.kind == 'PARAMS' and current_table:
                converter[current_table] = token.value
        converter.save()

def read_from_root():
    pass    
            
   
        

if __name__ == '__main__':
    parser.add_argument("mode", help="r/w")
    args = parser.parse_args()
    if args.mode == 'w':
        write_to_root('././conf.txt')
    elif args.mode == 'r':
        read_from_root()
        


    