from urllib import request

from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

# Create your views here.



def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['upload_input']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        print(name)



    return render(request, 'upload.html', context)