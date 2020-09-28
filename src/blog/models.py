from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL
# Create your models here.
class BlogPost(models.Model): # blogpost_set -> queryset
    user    = models.ForeignKey(User, default = 1,null = True, on_delete = models.SET_NULL)
    title   = models.CharField(max_length = 100)
    slug    = models.SlugField(unique =True) #hello world -> hello-world
    content = models.TextField(null = True, blank=True)
    publish_date= models.DateTimeField(auto_now=False, auto_now_add=False, null =True, blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    update      = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date', '-update', '-timestamp']
# 3 values curently ????? slug?
    def get_absolute_url(self):
        return f"/blog/{self.slug}"
    
    def get_edit_url(self):
        return f"/blog/{self.slug}/edit"

    def get_delete_url(self):
        return f"/blog/{self.slug}/delete"