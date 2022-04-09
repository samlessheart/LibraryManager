
from datetime import datetime
from email import message
from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from books.decorators import employee_required
from .models import PassBook
from books.models import Book
from django.db.models import F
from django.contrib.auth import get_user_model
User = get_user_model()
from .forms import borrowForm
from django.contrib import messages
from django.core.paginator import Paginator

@login_required(login_url='/user/login/')
def dashboard(request):
    if request.user.is_employee== True:
        return redirect('dashboard1')
    else:
        return redirect('profile')

@login_required(login_url='/user/login/')
@employee_required
def dashboard1(request, page=1):
    obj_pass = PassBook.objects.all().order_by(F('return_date').desc(nulls_first=True))
    paginator = Paginator(obj_pass, 7)

    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    
    return render(request, 'passbook/dashboard1.html', {'page_obj': page_obj})

@login_required(login_url='/user/login/')
def profile(request):
    obj_pass = PassBook.objects.filter(member=request.user).order_by(F('return_date').desc(nulls_first=True) )
    print(obj_pass)
    context= {'obj_pass':obj_pass}
    return render(request, 'passbook/profile.html',context=context )




@login_required(login_url='/user/login/')
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
            if member is not None and object_book.in_stock == True and member.profile.borrowed_book is None:
                passentry = PassBook.objects.create(member=member, book = object_book, staff=staff)
                object_book.in_stock = False
                object_book.save()
                prof = member.profile
                prof.borrowed_book = object_book
                prof.save()
                print(member.profile.borrowed_book)
                member.save()
                print(member.profile.borrowed_book)
                
                print (passentry)
                messages.success(request, f'{object_book} is leased to {member}')
                return redirect('booklist', 1)
                
            else:
                if member is None:
                    messages.warning(request, 'Member Not found.')
                elif member.profile.borrowed_book is not None:
                    messages.warning(request, 'Please return the due book before borrowing a new Book.')
                else:
                    messages.warning(request, 'This book is not available') 
            
    return render(request, 'passbook/borrow.html', context=context)


@login_required(login_url='/user/login/')
@employee_required
def book_return(request, pk):
    print('priniting pk pass obj')
    print(pk)
    pass_obj = PassBook.objects.get(id=pk)
    book_obj = Book.objects.get(id = pass_obj.book.id)
    book_obj.in_stock = True
    book_obj.save()
    pass_obj.return_date = datetime.now()
    pass_obj.complete = True
    user_obj = pass_obj.member
    prof_obj = user_obj.profile
    prof_obj.borrowed_book = None
    prof_obj.save()
    user_obj.save()
    pass_obj.save()
    
    messages.success(request, f'{pass_obj.member} has returned the {pass_obj.book.name}')

    return redirect('dashboard')

