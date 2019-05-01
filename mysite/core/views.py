from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy


from .forms import *
from .models import *

from django.contrib.auth import logout as auth_logout

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')


class Home(TemplateView):
    template_name = 'home.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)


def pdf_list(request):
    pdfs = PDF.objects.all()
    return render(request, 'pdf_list.html', {
        'pdf': pdfs
    })

def login(request):
    return render(request,'login.html')
def home(request):
    return render(request,'home.html')

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pdf_list')
    else:
        form = PDFForm()
    return render(request, 'upload_pdf.html', {
        'form': form
    })


def delete_pdf(request, pk):
    if request.method == 'POST':
        pdf = PDF.objects.get(pk=pk)
        pdf.delete()
    return redirect('pdf_list')


class pdfListView(ListView):
    model = PDF
    template_name = 'class_pdf_list.html'
    context_object_name = 'pdf'





class UploadView(CreateView):
    model = PDF
    form_class = PDFForm
    success_url = reverse_lazy('class_pdf_list')
    template_name = 'upload_pdf.html'
