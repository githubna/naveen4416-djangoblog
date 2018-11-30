"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib     import admin
from django.urls        import path,include
from django.conf.urls   import url

from django.conf             import settings
from django.conf.urls.static import static
from django.contrib.auth     import views as authviews
import os

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/',include('frontend.urls', namespace='frontend')),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^dashboard/',include('dashboard.urls', namespace='dashboard')),
    url(r'^users/',include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
