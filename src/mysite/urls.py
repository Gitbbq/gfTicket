"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from apps.Core.views import Index

urlpatterns = [
                  url(r'^admin/rq/', include('django_rq_dashboard.urls')),
                  url(r'^admin/', admin.site.urls),
                  url(r'^SSO/', include('apps.SSO.urls')),
                  url(r'^AttendanceSystem/', include('apps.AttendanceSystem.urls')),
                  url(r'^DownloadCenter/', include('apps.DownloadCenter.urls')),
                  url(r'^Document/', include('apps.Document.urls')),
                  url(r'^SupportTicketSystem/', include('apps.SupportTicketSystem.urls')),
                  url(r'^BusinessSystem/', include('apps.BusinessSystem.urls')),
                  url(r'^Equipment/', include('apps.Equipment.urls')),
                  url(r'^IPAddress/', include('apps.IPAddress.urls')),
                  url(r'^$', Index.as_view(), name="index"),
                  url(r'^django-rq/', include('django_rq.urls')),
              ] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
