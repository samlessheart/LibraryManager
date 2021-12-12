from django.conf import settings
from django.core import paginator
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .forms import borrowForm, bookForm
from .models import Author, Book, PassBook
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .decorators import employee_required
from django.contrib import messages
from django.db.models import F

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
    object = Book.objects.filter(id=pk)
    context = {'object':object}
    return render(request, 'books/bookdetail.html', context=context)


def authorlist(request, page=1):
    author_list = Author.objects.all().order_by('name')
    paginator = Paginator(author_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
      
    return render(request, 'books/authorlist.html', {'page_obj': page_obj})

@employee_required
def borrow(request, pk):
    form = borrowForm()
    object_book = Book.objects.get(id=pk)
    context = {'object_book':object_book, 'form':form}
    if request.method == 'POST':
        form = borrowForm(request.POST) 
        if form.is_valid():
            member = form.cleaned_data['member_id']  
            staff = request.user 
            try:                    
                member = User.objects.get(member_id= member)
            except:
                member = None
            if member is not None and object_book.in_stock == True:
                passentry = PassBook.objects.create(member=member, book = object_book, staff=staff)
                object_book.in_stock = False
                object_book.save()
                member.profile.borrowed_book = object_book
                member.save()
                
                print (passentry)
                messages.success(request, f'{object_book} is leased to {member}')
                return redirect('booklist', 1)
                
            else:
                if member is None:
                    messages.warning(request, 'Member Not found.')
                else:
                    messages.warning(request, 'book is not available') 
            
    return render(request, 'books/borrow.html', context=context)


@login_required
def dashboard(request):
    if request.user.is_employee== True:
        return redirect('dashboard1')
    else:
        return redirect('profile')

@employee_required
def dashboard1(request):
    obj_pass = PassBook.objects.all().order_by(F('return_date').desc(nulls_first=True))
    print(obj_pass)
    context= {'obj_pass':obj_pass}
    return render(request, 'books/dashboard1.html', context=context)

@login_required
def profile(request):
    obj_pass = PassBook.objects.filter(member=request.user).order_by(F('return_date').desc(nulls_first=True) )
    print(obj_pass)
    context= {'obj_pass':obj_pass}
    return render(request, 'books/profile.html',context=context )

@login_required
@employee_required
def add_book(request):
    form = bookForm()
    context = {'form':form}
    return render(request, 'books/add_book.html', context)