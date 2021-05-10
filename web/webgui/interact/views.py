from django.shortcuts import render, redirect
from .forms import ExtractForm, DownloadForm, ParseForm, ReleaseForm, \
    LoginForm
from core.models import Release, Files
from django.apps import apps
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, Http404
from django.views import View
from django.urls import reverse_lazy
from .scripts.extractor import Extractor, DateTimes, Run, FileName, \
    SearchDetails, VersionDetails
from .scripts.parser import handle_uploaded_file, ValidityDates, Runs, Filenames, \
    write_to_database
from django.http import FileResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage,\
    PageNotAnInteger, Page
from typing import Optional, Tuple, List
from django.db.models.query import QuerySet

extractor = Extractor()


class InteractLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('interact:login')


class InteractLoginView(LoginView):
    template_name = 'interact/login.html'
    redirect_authenticated_user = True
    authentication_form = LoginForm


class InteractLogoutView(InteractLoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('interact:login')


class PaginatedMixin:
    pages_per_pagination = 3
    records_per_page = 3
    
    def get_paginator(self, queryset: QuerySet, page: Optional[int]) -> Tuple[Page, List]:
        paginator = Paginator(queryset, self.records_per_page) 
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page = 1
            page_obj = paginator.page(page)
        except EmptyPage:
            page = paginator.num_pages
            page_obj = paginator.page(page)
        page = int(page)
        page_range = paginator.page_range[page - 1: page + self.pages_per_pagination - 1]
        if len(page_range) < self.pages_per_pagination:
            page_range = paginator.page_range[-self.pages_per_pagination:]
        return page_obj, page_range
    
    
@login_required(login_url=reverse_lazy('interact:login'))
@require_http_methods(['GET'])
def main(request):
    return render(
        request,
        'interact/base.html'
    )
    

class ReleaseView(PaginatedMixin, InteractLoginRequiredMixin, View):
    release_form_class = ReleaseForm
    template_name = 'interact/release.html'
    records_per_page = 10
        
    def get(self, request, *args, **kwargs):
        page = request.GET.get('page') 
        releases, page_range = self.get_paginator(Release.objects.all(), page)       
        release_form = self.release_form_class()
        return render(
            request,
            self.template_name,
            { 
                'release_form': release_form,
                'page_obj': releases,
                'page_range': page_range
            }
        )
    
    def post(self, request, *args, **kwargs):
        release_form = self.release_form_class(request.POST)
        saved = False
        if release_form.is_valid():
            release_form.save()
            saved = True
        releases, page_range = self.get_paginator(Release.objects.all(), 1)
        return render(
            request,
            self.template_name,
            {
                'release_form': release_form,
                'saved': saved,
                'page_obj': releases,
                'page_range': page_range
            }
        )


class FilesListView(PaginatedMixin, InteractLoginRequiredMixin, View):
    template_name = 'interact/files.html'
    records_per_page = 10
        
    def get(self, request, *args, **kwargs):
        page = request.GET.get('page') 
        releases, page_range = self.get_paginator(Files.objects.all(), page)       
        return render(
            request,
            self.template_name,
            { 
                'page_obj': releases,
                'page_range': page_range
            }
        )

        

class ParseView(InteractLoginRequiredMixin, View):
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
            release = Release.objects.filter(name=cd['release'])
            if not release:
                return render(
                    request,
                    self.template_name,
                    {
                        'parse_form': parse_form,
                        'error': ('The provided release does not exist.', )
                    }
                )
            release = release.first()  
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
                    except Exception:
                        error = ('Unable to extract validity dates from given parameters.', )
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
                        release=release,
                        version = cd.get('version'),
                        valid_from=valid_from,
                        valid_to=valid_to,
                        remarks=cd.get('remarks')
                    )
                    sent = True
                    
                except Exception:
                    error = ('''
                             Unable to write to the database. 
                             Check if all the constraints meet the requirements.''', )
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


@login_required(login_url=reverse_lazy('interact:login'))
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
    

class ExtractView(InteractLoginRequiredMixin, View):
    login_url=reverse_lazy('interact:login')
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