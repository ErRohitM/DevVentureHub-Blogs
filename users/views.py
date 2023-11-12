from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from . models import Bloger
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import datetime


def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        user_email = request.POST.get('email')
        contact = request.POST.get('contact')
        joined_at = datetime.datetime.now()
        #bloger_categery = request.POST.get('blog_type')
        
        if form.is_valid():
            user = form.save()
        
            Bloger.objects.create(username=user, bloger_email=user_email, contact_info=contact, join_date=joined_at)
            
            
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            authenticate(request, usename=username, password=password)        
            
            
            
            if user is not None:
                login(request, user)
                messages.info = (request, 'sucessfully created user')
                return redirect('home')
            else:
                messages.warning(request, 'please login with actual crediantials')
                return render(request, 'users/login.html')
        else:
            messages.warning(request, 'please check for user crediantials')
            return redirect('create_user')
    else:
        form = UserCreationForm()
        #messages.info(request, 'sorry unable to crete your account')
        return render(request, 'users/register.html', {'form': form})


            
        