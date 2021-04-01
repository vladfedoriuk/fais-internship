from django.shortcuts import render
from .forms import ExtractForm, DownloadForm
import core.models 
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.views import View
from .scripts.extractor import Extractor, DateTimes, Run, FileName, \
    SearchDetails, VersionDetails
from django.http import FileResponse

# Create your views here.
extractor = Extractor()

@require_http_methods(['GET', 'POST'])
def parse(request):
    return render(request, 'interact/parse.html')


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

class ExtractView(View):
    extract_form_class = ExtractForm
    download_form_class = DownloadForm
    template_name = 'interact/extract.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {
                'form': form
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