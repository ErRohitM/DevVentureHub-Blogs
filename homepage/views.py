import datetime
from django.shortcuts import render
from django.http import HttpResponse
from blog_page.models import Create_Blog
from django.utils import timezone
from datetime import timedelta
from users.models import Bloger
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    #start_date = datetime.datetime.now()
    #end_date = datetime.date(2023, 8, 10)
    #blog_list = Create_Blog.objects.filter(created_at__range=(start_date, end_date))
    blog_list = Create_Blog.objects.filter(created_at__day__gte=0)
    return render(request, 'home/index.html', {'blog':blog_list})
    

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def blog_post(request):
    blog_techno = Create_Blog.objects.filter(blog_categery='Techno')
    blog_personal = Create_Blog.objects.filter(blog_categery='Personal')
    blog_money = Create_Blog.objects.filter(blog_categery='Money')
    blog_world = Create_Blog.objects.filter(blog_categery='World')
    blog_design = Create_Blog.objects.filter(blog_categery='Design')
    blog_culture = Create_Blog.objects.filter(blog_categery='Culture')
    blog_politics = Create_Blog.objects.filter(blog_categery='Politics')
    blog_opinion = Create_Blog.objects.filter(blog_categery='Opinion')
    blog_science = Create_Blog.objects.filter(blog_categery='Science')
    blog_Health = Create_Blog.objects.filter(blog_categery='Health')
    blog_Travel = Create_Blog.objects.filter(blog_categery='Travel')
    blog_style = Create_Blog.objects.filter(blog_categery='Style')
    blog_business = Create_Blog.objects.filter(blog_categery='Business')
    
    context = {
        'techno_blog' : blog_techno,
        'personal_blog': blog_personal,
        'money_blog': blog_money,
        'world_blog': blog_world,
        'design_blog': blog_design,
        'culture_blog': blog_culture,
        'politics_blog': blog_politics,
        'opinion_blog': blog_opinion,
        'science_blog': blog_science,
        'health_blog': blog_Health,
        'travel_blog': blog_Travel,
        'style_blog': blog_style,
        'business_blog': blog_business
    }
    return render(request, 'home/blogspage.html', context)

    
def details(request, pk):
    post = get_object_or_404(Create_Blog, blog_id=pk)
    context = {'blog':post}
    return render(request, 'home/detailed.html', context)

