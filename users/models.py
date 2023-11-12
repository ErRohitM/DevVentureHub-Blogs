import uuid
from django.db import models
from django.contrib.auth.models import User



class Bloger(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4)
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='username_set')
    bloger_email = models.EmailField(max_length=100, unique=True, default= '@EmailField', null=False)
    contact_info = models.CharField(max_length=250, null=True, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)
    #bloger_categery = models.CharField(max_length=10, choices=blog_type)
   
    def __str__(self) -> str:
        return self.username.username