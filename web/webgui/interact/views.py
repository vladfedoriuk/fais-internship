from django.shortcuts import render
from .forms import ExtractForm
import core.models 
from django.views.decorators.http import require_http_methods
from django.views import View

# Create your views here.

    
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
            print(form.cleaned_data)
        return render(
            request,
            self.template_name,
            {
                'form': form
            }
        )