# Django markdown-editor

------------
The markdown editor widget for Django,you can use it in admin fields and forms,it is based on editor.md js plugins.


![](https://raw.githubusercontent.com/feiyin0719/django-markdown-editor/master/markdown.png)

## how to use
1.git clone https://github.com/feiyin0719/django-markdown-editor.git

2.copy markdown folder to your project

3.add markdown in your project settings.py, such as
```python

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'markdown',
)
```
4.use in admin.py
```python
class TestAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownWidget()},
    }
admin.site.register(Test,TestAdmin)
```
if you use xadmin,please use XAdminMarkdownWidget,such as:
```python
class TestAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': XAdminMarkdownWidget()},
    }
xadmin.site.register(Test,TestAdmin)
```
5.use in forms

```python
from django import forms

from markdown.forms import MarkdownField


class BlogForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    context = MarkdownField()
```
then in in templates,please add {{form.media}} in <head></head> to import js/css
```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <title>Hello Django!</title>
    {{form.media}}
</head>
<body>
{{form}}
</body>
</html>
```
6.how to upload image
include url in urls.py such as
```python
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HelloDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', view.hello),
    url(r'^markdown/', include('markdown.urls')),
)
```
7.upload image config
config upload image floder in settings.py
```python
MARKDOWN_IMAGE_FLODER='markdown'
```
config upload image format in settings.py
```python
MARKDOWN_IMAGE_FORMATS=["jpg", "jpeg", "gif", "png", "bmp", "webp"]
```
8.other config
when you create widget use params as editor.md
such as
```python
from django.contrib import admin

# Register your models here.
from django.db import models

from markdown.models import Test
from markdown.widgets import AdminMarkdownWidget


class TestAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownWidget(emoji=False)},
    }
admin.site.register(Test,TestAdmin)
```
the support params
```html
                    width   
                    height 
                    theme 
                    previewTheme
                    editorTheme 

                    syncScrolling
                    saveHTMLToTextarea 

                    emoji
                    taskList
                    tocm
                    tex

                    flowChart
                    sequenceDiagram
                    codeFold
                  


```
you can refer to editor.md http://pandao.github.io/editor.md/
