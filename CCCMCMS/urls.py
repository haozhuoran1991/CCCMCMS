"""CCCMCMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from DjangoUeditor import urls as DjangoUeditor_urls
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.index', name='index'),
    url(r'^fellowship/', 'fellowship.views.fellowship_detail', name='fellowship'),
    url(r'^contact/', 'home.views.contact', name='contact'),
    url(r'^ueditor/', include(DjangoUeditor_urls)),
]


# if settings.DEBUG:
#     from django.conf.urls.static import static
#     urlpatterns += static(
#         settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
#     )



if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)