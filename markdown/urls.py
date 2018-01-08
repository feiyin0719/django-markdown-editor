from django import VERSION
from markdown.views import upload_image
if  VERSION<(1,9):
    from django.conf.urls import patterns, url
    urlpatterns = patterns('',
        url(r'^uploadimage/$', upload_image),
    )
else:
    from django.conf.urls import  url
    urlpatterns=[
        url(r'^uploadimage/$', upload_image),
    ]
