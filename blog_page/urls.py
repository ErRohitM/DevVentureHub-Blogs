from django.urls import path
from . views import create_blog

urlpatterns = [
    path('create_blog/', create_blog, name='create_blog'),
]


