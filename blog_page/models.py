import uuid
from django.db import models
from users.models import Bloger


class Create_Blog(models.Model):
    blog_type = {
        ('World', 'World'),
        ('Design', 'Design'),
        ('Culture', 'Culture'),
        ('Politics', 'Politics'),
        ('Opinion', 'Opinion'),
        ('Science', 'Science'),
        ('Health', 'Health'),
        ('Travel', 'Travel'),
        ('Style', 'Style'),
        ('Personal', 'Personal'),
        ('Techno', 'Techno'),
        ('Money', 'Money'),
        ('Business', 'Business')
    }
    blog_id = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_length=100, verbose_name='blog_name')
    blog_image = models.ImageField(upload_to='blog_images/')
    created_by = models.ForeignKey(Bloger, on_delete=models.CASCADE, unique=False, related_name='bloger_set')
    created_at = models.DateField(auto_now_add=True)
    blog_categery = models.CharField(max_length=10, choices=blog_type)
    content = models.TextField()
    
    def __str__(self):
        return self.title
       
    
    
    
    