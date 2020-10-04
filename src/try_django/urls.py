from django.conf import settings

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


if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    