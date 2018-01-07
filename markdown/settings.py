from django.conf import settings


MARKDOWN_WIDGET_TEMPLATE = getattr(
  settings, "MARKDOWN_WIDGET_TEMPLATE", "markdown/widgets/markdown.html")
MARKDOWN_IMAGE_FORMATS = getattr(settings, "MARKDOWN_IMAGE_FORMATS", ["jpg", "jpeg", "gif", "png", "bmp", "webp"])
MARKDOWN_UP_IMAGE_URL=getattr(settings, "MARKDOWN_UP_IMAGE_URL", "/markdown/uploadimage/")
MARKDOWN_IMAGE_FLODER=getattr(settings, "MARKDOWN_IMAGE_FLODER", "markdown")
MEDIA_URL=getattr(settings, "MEDIA_URL", "/media/")
MEDIA_ROOT=getattr(settings, "MEDIA_ROOT", "./media")
STATIC_URL=getattr(settings, "STATIC_URL", "/static/")