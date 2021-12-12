from django.conf import settings
from django.core import paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from .forms import bookForm
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
    return render(request, 'books/add_book.html', context)




def search_book(request, qs):
    books_obj = Book.objects.filter(name__icontains = qs)
    authur_obj = Author.objects.filter(name__icontains = qs)

