from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('image_upload', views.image_upload, name='image'),
    path('pdf_upload', views.pdf_upload, name='pdf'),
    path('docx_upload', views.docx_upload, name='docx'),
    path('download', views.download_text, name='download_text'),
]

# Add this line to serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)