from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL
# Create your models here.
class BlogPost(models.Model): # blogpost_set -> queryset
    user    = models.ForeignKey(User, default = 1,null = True, on_delete = models.SET_NULL)
    title   = models.CharField(max_length = 100)
    slug    = models.SlugField(unique =True) #hello world -> hello-world
    content = models.TextField(null = True, blank=True)
    
# 3 values cureently ????? slug?