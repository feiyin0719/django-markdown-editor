from django import VERSION, forms
from django.contrib.admin import widgets as admin_widgets
from django.utils.html import conditional_escape
from django.template import Context, loader
from django.conf import settings
# Django 1.7 compatibility
from markdown.utils import compatible_staticpath
from  markdown import settings as markdown_settings
try:
    from django.forms.utils import flatatt
except ImportError:
    from django.forms.util import flatatt




# Python 3 compatibility
# https://docs.djangoproject.com/en/1.5/topics/python3/#string-handling
try:
    from django.utils.encoding import force_unicode
except ImportError:
    from django.utils.encoding import force_text as force_unicode


class MarkdownWidget(forms.Textarea):

    def __init__(self, *args, **kwargs):
        self.template = kwargs.pop(
            "template", markdown_settings.MARKDOWN_WIDGET_TEMPLATE)
        self.lib=markdown_settings.STATIC_URL+"markdown/lib/"
        self.width=kwargs.pop("width","100%")
        self.height = kwargs.pop("height", "540")
        self.syncScrolling=kwargs.pop("syncScrolling","single")
        self.saveHTMLToTextarea=kwargs.pop("saveHTMLToTextarea",True)
        self.emoji=kwargs.pop("emoji",True)
        self.taskList=kwargs.pop("taskList",True)
        self.tocm=kwargs.pop("tocm",True)
        self.tex=kwargs.pop("tex",True)
        self.flowChart=kwargs.pop("flowChart",True)
        self.sequenceDiagram=kwargs.pop("sequenceDiagram",True)
        self.codeFold=kwargs.pop("codeFold",True)
        self.imageUpload=kwargs.pop("imageUpload",True)
        self.imageFormats=kwargs.pop("imageFormats",markdown_settings.MARKDOWN_IMAGE_FORMATS)
        self.imageUploadURL=kwargs.pop("imageUploadURL",markdown_settings.MARKDOWN_UP_IMAGE_URL)
        self.theme=kwargs.pop("theme", "light")
        self.previewTheme=kwargs.pop("previewTheme","light")
        self.editorTheme=kwargs.pop("editorTheme", "paraiso-light")
        super(MarkdownWidget, self).__init__(*args, **kwargs)

    def _media(self):
        return forms.Media(
            css={
                "all": (compatible_staticpath("markdown/css/editormd.css"),)
            },
            js=(
                compatible_staticpath("markdown/js/jquery.min.js"),
                compatible_staticpath("markdown/js/editormd.min.js"),

            ))
    media = property(_media)

    def render(self, name, value, attrs=None):
        if value is None:
            value = ""
        if VERSION < (1, 11):
            final_attrs = self.build_attrs(attrs, name=name)
        else:
            final_attrs = self.build_attrs(attrs, {'name': name})

        if "class" not in final_attrs:
            final_attrs["class"] = ""
        final_attrs["class"] += " wmd-input"
        template = loader.get_template(self.template)

        # Compatibility fix:
        # see https://github.com/timmyomahony/django-pagedown/issues/42
        # imageFormats_str=','.join('"'+i+'"' for i in self.imageFormats)
        # imageFormats_str='['+imageFormats_str+']'
        markdown_conf={
            'width':self.width,
            'height':self.height,
            'syncScrolling': self.syncScrolling,
            'saveHTMLToTextarea'   : self.saveHTMLToTextarea,
            'emoji':self.emoji,
            'taskList':self.taskList,
            'tocm':self.tocm,
            'tex':self.tex,
            'flowChart':self.flowChart,
            'sequenceDiagram':self.sequenceDiagram,
            'codeFold':self.codeFold,
            'imageUpload':self.imageUpload,
            'imageFormats':self.imageFormats,
            'imageUploadURL':self.imageUploadURL,
            'theme': self.theme,
            'previewTheme': self.previewTheme,
            'editorTheme':self.editorTheme,

        }

        context = {
            "attrs": flatatt(final_attrs),
            "body": conditional_escape(force_unicode(value)),
            "id": final_attrs["id"],
            "marklib":self.lib,
            "markdownconf":markdown_conf,
        }
        context = Context(context) if VERSION < (1, 9) else context
        return template.render(context)

class AdminMarkdownWidget(MarkdownWidget, admin_widgets.AdminTextareaWidget):
    def __init__(self, *args, **kwargs):
        super(AdminMarkdownWidget, self).__init__(*args, **kwargs)
class XAdminMarkdownWidget(AdminMarkdownWidget):
    def __init__(self, *args, **kwargs):
        super(XAdminMarkdownWidget, self).__init__(*args, **kwargs)
    def _media(self):
        return  forms.Media(
            css={
                "all": (compatible_staticpath("markdown/css/editormd.css"),)
            },
            js=(
                compatible_staticpath("markdown/js/editormd.min.js"),
            ))
    media = property(_media)