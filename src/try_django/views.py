from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


from .forms import ContactForm
from blog.models import BlogPost



def home_page(request):
    my_title = "Hello there"
    qs = BlogPost.objects.all()[:5]
    context = {"title": "Welcome to Try Django", 'blog_list': qs}
    return render(request, "home.html", context)

def about_page(request):
    return HttpResponse("<h1>helloWorld</h1>")

def contact_page(request):
    form = ContactForm(request.POST or None)
    print(form.is_valid)
    if form.is_valid():
        # print(form.cleaned_data)
        form = ContactForm() # 새로 초기화 해주는구만
    context = {
         "title": "Contact us",
         "form": form,
    }
    return render(request, "form.html", context)


def example_page(request):
    my_title = "Hello there"
    context         = {"title": my_title}
    template_name   = "hello_world.html"
    template_obj    = get_template(template_name)
    rendered_item   = template_obj.render(context)
    return HttpResponse(rendered_item)