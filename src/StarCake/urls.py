from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from posts.views import index,blog,post,search,contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('blog/',blog,name ='post_list'),
    path('search/',search,name='search'),
    path('post/<id>/',post,name='post_details'),
    path('tinymce/', include('tinymce.urls')),
    path('contact/',contact,name='contact'),
]


urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
