from django.shortcuts import redirect, render
from .forms import SignupForm, profileForm, LoginForm
from .models import MyUser, Profile

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


@login_required 
def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            member_id = form.cleaned_data['member_id']
            phone = form.cleaned_data['phone']
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            password = form.cleaned_data['password']            
            user = MyUser.objects.create_user(email, member_id, 
                                            phone=phone, fname=fname, lname=lname, password=password)
            
            prof_obj = Profile()
            prof_obj.user = user
            prof_obj.save()
            messages.success(request, f'Member is added with {member_id}')
            return redirect('home')
    return render(request, 'members/signup.html', {'form':form})

def signin(request):
    form = LoginForm()
    context = {'form':form}

    if request.method== 'POST':
        form =LoginForm(request.POST)
        if form.is_valid():           
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user) 
                messages.success(request, 'You are logged in')               
                return redirect('home', ) 
            else:
                messages.warning(request, 'Please Enter correct credentials')
        else:
                messages.warning(request, 'Please Enter correct credentials')
        
    return render(request, 'members/signin.html', context)

@login_required 
def signout(request):
    logout(request)
    messages.info(request, 'You are logged out')  
    return redirect('home',) 


def profile(request):
    return render(request, 'members/common.html')


def update(request):
    return render(request, 'members/common.html')



    

