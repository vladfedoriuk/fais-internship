The repository for the parameters parsing/extracting scripts. 
## Scripts

- *parser.py* is meant to parse and convert a configuration file into the database tables records
- *extractor.py* is meant to extract the configurations into a single text file

- To use the scripts, you need to get **pyenv** installed on your local machine: https://realpython.com/intro-to-pyenv/
- When done, create and activate virtual environment:
    
    1. `pyenv install 3.9.1` - install python 3.9.1

    2. `pyenv virtualenv 3.9.1 <environment name>` - create a virtual environment

    3. `pyenv local <environment name>` - activate it

    4. `pip install -r requirements.txt` - install the requirements

- The scripts use SQLAlchemy to communicate with a database. They **require from you** to set some environment variables:
    `export username=<your mysql username>`
    `export password=<your mysql password>`

- To know more about the functionalities of the scripts:
    `python3 scripts/parser.py -h`
    `python3 scripts/extractor.py -h`
    
- The output of the preceding commands should look as follows:
    ```
    python scripts/parser.py -h
    usage: parser.py [-h] [-rf RUNFROM] [-rt RUNTO] [-ff FILEFROM] [-ft FILETO]
                 [-vf VALIDFROM] [-vt VALIDTO] [--remarks REMARKS]
                 conf version

    positional arguments:
    conf                  The name of the configuration file
    version               The version of the configuration

    optional arguments:
    -h, --help            show this help message and exit
    -rf RUNFROM, --runfrom RUNFROM
                        The run from which the configuration is valid
    -rt RUNTO, --runto RUNTO
                        The run up to which the configuration is valid
    -ff FILEFROM, --filefrom FILEFROM
                        The run file from which the configuration is valid
    -ft FILETO, --fileto FILETO
                        The run file up to which the configuration is valid
    -vf VALIDFROM, --validfrom VALIDFROM
                        The datetime from which the configuration is valid
                        Accepted patterns:
                        ['[yyyy]-[mm]-[dd]T[HH]:[MM]:[+-][HHMM]',
                        '[yyyy]-[mm]-[dd]', '[yyyy]-[mm]-[dd]T[HH]:[MM]:[SS]',
                        '[yyyy]-[mm]-[dd]T[HH]:[MM]:[SS][+-][HHMM]',
                        '[yyyy]-[mm]-[dd]T[HH]:[MM]']
    -vt VALIDTO, --validto VALIDTO
                        The datetime up to which the configuration is valid
                        Accepted patterns:
                        ['[yyyy]-[mm]-[dd]T[HH]:[MM]:[+-][HHMM]',
                        '[yyyy]-[mm]-[dd]', '[yyyy]-[mm]-[dd]T[HH]:[MM]:[SS]',
                        '[yyyy]-[mm]-[dd]T[HH]:[MM]:[SS][+-][HHMM]',
                        '[yyyy]-[mm]-[dd]T[HH]:[MM]']
    --remarks REMARKS, -r REMARKS
                        The optional remarks about the configuration version
    ```
    ```
    python scripts/extractor.py -h
    usage: extractor.py [-h] [--validfrom VALIDFROM] [--validto VALIDTO]
                    [-v VERSION] [-n NAME] [-r RUN] [-f FILE]

    optional arguments:
    -h, --help            show this help message and exit
    --validfrom VALIDFROM, -vf VALIDFROM
                        The date the configuration is valid from
                        ['[yyyy]-[mm]-[dd]T[HH]:[MM]:[SS]',
                        '[yyyy]-[mm]-[dd]',
                        '[yyyy]-[mm]-[dd]T[HH]:[MM]:[+-][HHMM]',
                        '[yyyy]-[mm]-[dd]T[HH]:[MM]',
                        '[yyyy]-[mm]-[dd]T[HH]:[MM]:[SS][+-][HHMM]']
    --validto VALIDTO, -vt VALIDTO
                        The date the configuration is valid to
                        ['[yyyy]-[mm]-[dd]T[HH]:[MM]:[SS]',
                        '[yyyy]-[mm]-[dd]',
                        '[yyyy]-[mm]-[dd]T[HH]:[MM]:[+-][HHMM]',
                        '[yyyy]-[mm]-[dd]T[HH]:[MM]',
                        '[yyyy]-[mm]-[dd]T[HH]:[MM]:[SS][+-][HHMM]']
    -v VERSION, --version VERSION
                        The version of the configurations
    -n NAME, --name NAME  The name of the output file
    -r RUN, --run RUN     The run id to extract datetimes from
    -f FILE, --file FILE  The run file name to extract datetimes from
    ```
