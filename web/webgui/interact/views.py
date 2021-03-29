from django.shortcuts import render
from .forms import ExtractForm
import core.models 

# Create your views here.

    
def parse(request):
    return render(request, 'interact/parse.html')

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