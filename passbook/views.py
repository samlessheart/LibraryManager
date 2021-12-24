
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from books.decorators import employee_required
from .models import  PassBook
from books.models import Book
from django.db.models import F
from django.contrib.auth import get_user_model
User=get_user_model()
from .forms import borrowForm
from django.contrib import messages

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
    return render(request, 'passbook/dashboard1.html', context=context)

@login_required
def profile(request):
    obj_pass = PassBook.objects.filter(member=request.user).order_by(F('return_date').desc(nulls_first=True) )
    print(obj_pass)
    context= {'obj_pass':obj_pass}
    return render(request, 'passbook/profile.html',context=context )





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
            
    return render(request, 'passbook/borrow.html', context=context)

