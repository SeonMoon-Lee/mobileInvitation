"""
URL configuration for MobileInvitation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf.urls import (
    handler400, handler404, handler500
)
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from django.views.generic import RedirectView
from django.views.static import serve

from MobileInvitation import settings
from MobileInvitation.views import custom_page_not_found, error500

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='accountapp:login', permanent=False)),
    path('admin/', admin.site.urls),
    path('accounts/', include('accountapp.urls')),
    path('invitation/', include('invitationapp.urls')),
    #path('comments/', include('commentapp.urls')),
    path('summernote/', include('django_summernote.urls')),

    url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = custom_page_not_found