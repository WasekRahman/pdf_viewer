from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import *
from django.contrib.auth import logout
from mysite.core import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    path('home/', views.home, name='home'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^logout/$', views.logout, name='logout'),
    #url(r'^management/logout/$', 'django.contrib.auth.views.logout'),
    #url(r'^auth/disconnect/(?P<id>\d+)/$', include('social_django.urls', namespace='social')),
    path('pdf/', views.pdf_list, name='pdf_list'),
    path('pdf/upload/', views.upload_pdf, name='upload_pdf'),
    path('pdfs/<int:pk>/', views.delete_pdf, name='delete_pdf'),
    path('login/', views.login, name='login'),
    path('class/pdfs/', views.pdfListView.as_view(), name='class_pdf_list'),
    path('class/pdfs/upload/', views.UploadView.as_view(), name='class_upload_pdf'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
