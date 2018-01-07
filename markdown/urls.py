from django.conf.urls import patterns, url

from markdown.views import upload_image

urlpatterns = patterns('',
    url(r'^uploadimage/$', upload_image),
)
