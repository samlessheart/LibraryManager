from django.conf import settings
from django.core import paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from .forms import bookForm, authorForm
from .models import Author, Book
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .decorators import employee_required
from django.contrib import messages
from django.db.models import F
from itertools import chain

#User = settings.AUTH_USER_MODEL
User=get_user_model()

# Create your views here.


def home(request, ):
    object = Book.objects.filter(genre ='stories')
    context = {'object': object, }
    return render (request, 'books/home.html', context)


def booklist(request, page=1):
    Book_list = Book.objects.all().order_by('doc_id')
    paginator = Paginator(Book_list, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
      
    return render(request, 'books/booklist.html', {'page_obj': page_obj})


def bookdetail(request, pk):
    context = {'object':get_object_or_404(Book, pk)}
    return render(request, 'books/bookdetail.html', context=context)
    


def authorlist(request, page=1):
    author_list = Author.objects.all().order_by('name')
    paginator = Paginator(author_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
      
    return render(request, 'books/authorlist.html', {'page_obj': page_obj})


def authordetail(request, pk):
    context = {'object':get_object_or_404(Author, pk)}
    return render(request, 'books/authordetail.html', context=context)




@login_required
@employee_required
def add_book(request):
    form = bookForm()
    context = {'form':form}
    if request.method == 'POST':
        form = bookForm(request.POST)
        if form.is_valid():
            print("true")
            print(f"----{form}----")
            docid = form.cleaned_data['doc_id']
            name = form.cleaned_data['name']
            author = form.cleaned_data['author']
            price = form.cleaned_data['price']
            pages = form.cleaned_data['pages']
            genre = form.cleaned_data['genre']
            tags = form.cleaned_data['tags']
            published = form.cleaned_data['published']
            publication = form.cleaned_data['publication']
            vendor = form.cleaned_data['vendor']

            abook = Book.objects.create(doc_id= docid, name= name, author=author, 
                            price= price, pages= pages, genre= genre, tags=tags, published= published,
                                publication= publication, vendor= vendor)
            abook.save()
            messages.success(request, f'{abook.name} is added successfully.')

        else:
           messages.warning(request, 'Something went wrong.') 

    return render(request, 'books/add_book.html', context)



@login_required
@employee_required
def add_author(request):
    form = authorForm()
    context = {'form':form}
    if request.method == 'POST':
        form = authorForm(request.POST)
        if form.is_valid:
            name= form.cleaned_data['name']
            dob= form.cleaned_data['dob']
            doe= form.cleaned_data['doe']
            detail= form.cleaned_data['detail']

            anauthor = Author.objects.create(name= name, dob= dob, doe= doe, detail= detail)
            anauthor.save()
            messages.success(request, f'{anauthor.name} is added successfully.')
        else:
             messages.warning(request, 'Something went wrong.')

    return render(request, 'books/add_author.html', context)


def search_book(request, qs):
    books_obj = Book.objects.filter(name__icontains = qs)
    authur_obj = Author.objects.filter(name__icontains = qs)



