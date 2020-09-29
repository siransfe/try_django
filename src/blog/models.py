from django.conf import settings
from django.db import models
from django.utils import timezone


User = settings.AUTH_USER_MODEL
# Create your models here.

class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        # BlogPost.objects.all()
        return self.filter(publish_date__lte =now)    
    
    
class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)
    
    def published(self):
        return self.get_queryset().published()


class BlogPost(models.Model): # blogpost_set -> queryset
    user    = models.ForeignKey(User, default = 1,null = True, on_delete = models.SET_NULL)
    image = models.FileField(upload_to = 'image/', blank=True, null=True)
    title   = models.CharField(max_length = 100)
    slug    = models.SlugField(unique =True) #hello world -> hello-world
    content = models.TextField(null = True, blank=True)
    publish_date= models.DateTimeField(auto_now=False, auto_now_add=False, null =True, blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    update      = models.DateTimeField(auto_now=True)

    
    objects = BlogPostManager()
    class Meta:
        ordering = ['-publish_date', '-update', '-timestamp']
# 3 values curently ????? slug?
    def get_absolute_url(self):
        return f"/blog/{self.slug}"
    
    def get_edit_url(self):
        return f"/blog/{self.slug}/edit"

    def get_delete_url(self):
        return f"/blog/{self.slug}/delete"