from users.models import Bloger
from django.shortcuts import render, redirect
from . form import create_blog_form
import datetime
from django.http import HttpResponse

def create_blog(request):
    if request.method == 'POST':
        form = create_blog_form(request.POST, request.FILES)
        
        if form.is_valid():
            blogs = form.save(commit = False)
            bloger, created = Bloger.objects.get_or_create(username=request.user) 
            blogs.created_by = bloger
            blogs.created_at = datetime.datetime.now()
            blogs.save()
            return redirect('blog_post')
        
        else:
            print(form.errors)  
    else:
        form = create_blog_form()
        return render(request, 'blogs/create_blog.html', {'form':form})
    
