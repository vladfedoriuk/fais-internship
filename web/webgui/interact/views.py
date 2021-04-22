from django.shortcuts import render
from .forms import ExtractForm, DownloadForm, ParseForm, ReleaseForm
import core.models 
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, Http404
from django.views import View
from .scripts.extractor import Extractor, DateTimes, Run, FileName, \
    SearchDetails, VersionDetails
from .scripts.parser import handle_uploaded_file, ValidityDates, Runs, Filenames, \
    write_to_database

from django.http import FileResponse

extractor = Extractor()

class ReleaseView(View):
    release_form_class = ReleaseForm
    template_name = 'interact/release.html'
    
    def get(self, request, *args, **kwargs):
        release_form = self.release_form_class()
        return render(
            request,
            self.template_name,
            {
                'release_form': release_form
            }
        )
    
    def post(self, request, *args, **kwargs):
        release_form = self.release_form_class(request.POST)
        saved = False
        if release_form.is_valid():
            release_form.save()
            saved = True
        return render(
            request,
            self.template_name,
            {
                'release_form': release_form,
                'saved': saved
            }
        )
        

class ParseView(View):
    parse_form_class = ParseForm
    template_name = 'interact/parse.html'
    
    def get(self, request, *args, **kwargs):
        parse_form = self.parse_form_class()
        return render(
            request,
            self.template_name,
            {
                'parse_form': parse_form
            }
        )
    
    def post(self, request, *args, **kwargs):
        parse_form = self.parse_form_class(request.POST, request.FILES)
        
        sent = False

        if parse_form.is_valid():
            cd = parse_form.cleaned_data
            conf_file = handle_uploaded_file(cd['configuration'])
            
            valid_from = cd.get('valid_from')
            valid_to = cd.get('valid_to')
            if not valid_from and not valid_to:
                vd = ValidityDates()
                
                run_from = cd.get('run_from')
                run_to = cd.get('run_to')
                filename_from = cd.get('filename_from')
                filename_to = cd.get('filename_to')
                arg = None
                
                if run_from and run_to:
                    arg = Runs(run_from, run_to)
                elif filename_from and filename_to:
                    arg = Filenames(filename_from, filename_to)
                    
                if arg:
                    try:
                        valid_from, valid_to = vd.from_params(arg)
                    except Exception as e:
                        error = e.args
                        return render(
                            request,
                            self.template_name,
                            {
                                'parse_form': parse_form,
                                'error': error
                            }
                        )
            
            if valid_from and valid_to:
                try:
                    write_to_database(
                        conf_file_path=conf_file,
                        version = cd.get('version'),
                        valid_from=valid_from,
                        valid_to=valid_to,
                        remarks=cd.get('remarks')
                    )
                    sent = True
                except Exception as e:
                    error = e.args
                    return render(
                        request,
                        self.template_name,
                        {
                            'parse_form': parse_form,
                            'error': error
                        }
                    )
                    
            else:
                return render(
                        request,
                        self.template_name,
                        {
                            'parse_form': parse_form,
                            'error': ('Failed to extract some of the validity dates.',)
                        }
                    )
                
        return render(
            request,
            self.template_name,
            {
                'parse_form': parse_form,
                'sent': sent
            }
        )


@require_http_methods(['POST'])
def download(request):
    form = DownloadForm(request.POST)
    if form.is_valid():
        details = SearchDetails(
            form.cleaned_data['valid_from'],
            form.cleaned_data['valid_to'],
            form.cleaned_data['version']
        )
        filename = extractor.write_to_file(details)
        return FileResponse(open(filename, 'rb'), as_attachment=True)
    raise Http404('validity dates or version are not valid')
    

class ExtractView(View):
    extract_form_class = ExtractForm
    download_form_class = DownloadForm
    template_name = 'interact/extract.html'
    
    def get(self, request, *args, **kwargs):
        extract_form = self.extract_form_class()
        return render(
            request,
            self.template_name,
            {
                'extract_form': extract_form
            }
        )
    
    def post(self, request, *args, **kwargs):
        extract_form = self.extract_form_class(request.POST)
        download_form = self.download_form_class()
        
        versions_table = None 
        version_exists=True
        
        if extract_form.is_valid():
            cd = extract_form.cleaned_data
            valid_from = cd.get('valid_from')
            valid_to = cd.get('valid_to')
            version = cd.get('version')
            filename = cd.get('filename')
            run = cd.get('run')
                        
            if valid_from and valid_to:
                param = DateTimes((valid_from, valid_to))
            elif run:
                param = Run(run)
            elif filename:
                param = FileName(filename)
            
            available_versions = extractor.process(param)
            if version:
                version_exists = extractor.version_exists(available_versions, version)
                if version_exists:
                    versions_table = extractor.filter_by_version(available_versions, version)
            if not version or not version_exists:
                version_exists = False
                versions_table = available_versions
                
            versions_table = extractor.convert_datetimes(versions_table)
            print(versions_table)
    
        return render(
            request,
            self.template_name,
            {  
                'extract_form': extract_form,
                'download_form': download_form,
                'versions': versions_table,
                'version_exists': version_exists,
            }
        )