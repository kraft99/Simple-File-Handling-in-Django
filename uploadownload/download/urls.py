from django.urls import path, re_path
from . import views

# namespace
app_name = 'download'

urlpatterns = [

    re_path(r'^download/(?P<file_path>.*)/$', views.file_download, name='file_download'),

]
