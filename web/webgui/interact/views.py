from django.shortcuts import render
from .forms import ExtractForm
import core.models 
from django.views.decorators.http import require_http_methods
from django.views import View
from .scripts.extractor import Extractor

# Create your views here.

@require_http_methods(['GET', 'POST'])
def parse(request):
    return render(request, 'interact/parse.html')


@require_http_methods(['GET', 'POST'])
def extract(request):
    if request.method == 'POST':  
        form = ExtractForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ExtractForm()    
    return render(
        request, 
        'interact/extract.html',
        {
            'form': form
        }
    )


class ExtractView(View):
    form_class = ExtractForm
    template_name = 'interact/extract.html'
    extractor = Extractor()
    
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
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            valid_from = cd.get('valid_from')
            valid_to = cd.get('valid_to')
            version = cd.get('version')
            run = cd.get('run')
            filename = cd.get('filename')
            
            versions_table = None 
            params = None
            
            if valid_from and valid_to:
                available_versions = self.extractor.process_dates(valid_from, valid_to)
            elif run:
                available_versions = self.extractor.process_run(run)
            elif filename:
                available_versions = self.extractor.process_run(filename)
                
            if version:
                params = self.extractor.params_for_version(
                    available_versions, version)
                # process params, return file
                
            if not params or not version:
                versions_table = available_versions
                
        return render(
            request,
            self.template_name,
            {  
                'form': form,
                'versions': versions_table
            }
        )