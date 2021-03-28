from django.shortcuts import render
from .forms import ExtractForm

# Create your views here.

def parse(request):
    return render(request, 'interact/parse.html')

def extract(request):
    if request.method == 'POST':  
        form = ExtractForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ExtractForm()    
    return render(
        request, 
        'interact/extract.html',
        {
            'form': form
        }
    )