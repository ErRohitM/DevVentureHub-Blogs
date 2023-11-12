from django.urls import path
from . views import home,about,contact,blog_post, details

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contaact/', contact, name='contact'),
    path('blog_post/', blog_post, name='blog_post'),
    path('details/<str:pk>', details, name='details'),
]
