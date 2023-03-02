from blog import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('add-post/', views.addNewPost, name = 'add_post'),
    path('<slug:slug>', views.post_details, name = 'post_details'),
    path('delete-blog-post/<slug:slug>/', views.delete_post,name='delete_blog_post'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


