from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from .forms import BlogPostForm, BlogPostModelForm
from .models import BlogPost

#get -> 1 object
#filter -> [] objects

def blog_post_detail_page (request, slug):
    print("DJANGO SAYS: ", request.method, request.path, request.user)
    queryset = BlogPost.objects.filter(slug = slug)
    #if queryset.count() == 0:
    #    raise Http404
    #else:
    #    obj = BlogPost.objects.get(slug=slug)
    #여기다가 timezone을 통한 설정을 하게 되면, 항상 이 코드를 실행하게 된다는 문제가 있다. 
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog_post_detail_page.html"
    context = {"object": obj}
    return render(request, template_name, context)

def blog_post_list_view (request):
    # list out objects
    # could be search
    qs = BlogPost.objects.published() # queryset -> list of python object
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    #.published() > custom querySet.
    #qs = BlogPost.objects.filter(title__icontains = 'hello')
    template_name = 'blog/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

@staff_member_required
def blog_post_create_view(request):
    #form = BlogPostForm(request.POST or None)
    
    if not request.user.is_authenticated:
        return render(request, "not-a-user.html", {})
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        #print(form.cleaned_data) #dic datas
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        #form.save()
        form = BlogPostModelForm()
        #title = form.cleaned_data['title']
        #obj = BlogPost.objects.create(**form.cleaned_data)
        #obj = BlogPostForm()
    template_name = 'form.html'
    context = {'form': form}
    return render(request, template_name, context)

def blog_post_detail_view (request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/detail.html"
    context = {"object": obj}
    return render(request, template_name, context)

@staff_member_required
def blog_post_update_view (request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance = obj)
    if form.is_valid():
        print("changeD???")
        form.save()
    template_name = "form.html"
    context = {'form':form, "title": f"Update {obj.title}"}
    return render(request, template_name, context)

@staff_member_required
def blog_post_delete_view (request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/delete.html"
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")

    context = {"object": obj}
    return render(request, template_name, context)
