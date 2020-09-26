from django.contrib import admin
from django.urls import path, include
from .views import home_page, about_page, contact_page, example_page
from blog.views import blog_post_create_view


urlpatterns = [
    path('', home_page),
    
    path('blog/', include('blog.urls')),
    path('blog-new/',  blog_post_create_view),

    path('about/', about_page),
    path('contact/', contact_page),
    path('admin/', admin.site.urls),
]
