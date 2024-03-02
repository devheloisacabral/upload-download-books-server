from urllib import request

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from .models import Book

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

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('book_list')
    else:
        form = BookForm()

    return render(request, 'upload_book.html', {'form': form}) #aqui nós criamos o nome que vamos chamar no template

def book_list(request): #função que lista os dados recuperados do upload_book
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books}) #vamos chamar no template como books

