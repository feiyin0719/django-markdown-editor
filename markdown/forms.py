from django import forms

from .widgets import XAdminMarkdownWidget, MarkdownWidget, AdminMarkdownWidget


class MarkdownField(forms.CharField):

    """ A simple CharField that allows us avoid having to write widget code """

    widget = MarkdownWidget

class AdminMarkdownField(forms.CharField):

    """ A simple CharField that allows us avoid having to write widget code """

    widget = AdminMarkdownWidget
class XAdminMarkdownField(forms.CharField):

    """ A simple CharField that allows us avoid having to write widget code """

    widget = XAdminMarkdownWidget


# try:
#     from south.modelsinspector import add_introspection_rules
#     add_introspection_rules([], ["^markdown\.forms\.MarkdownField"])
#     add_introspection_rules([], ["^markdown\.forms\.AdminMarkdownField"])
# except ImportError:
#     raise
