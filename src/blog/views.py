from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BlogPost

#get -> 1 object
#filter -> [] objects
def blog_post_detail_page (request, slug):
    queryset = BlogPost.objets.filter(slug = slug)
    #obj = get_object_or_404(BlogPost, id = id)
    template_name = "blog_post_detail_page.html"
    context = {"object": obj}
    return render(request, template_name, context)