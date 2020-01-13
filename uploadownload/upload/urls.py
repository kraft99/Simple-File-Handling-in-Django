from django.urls import path,re_path
from upload import views


app_name = 'upload'

urlpatterns = [
    path('upload/',views.upload_view,name='upload'),
    path('upload-file/',views.upload_raw_file,name='upload-file'),
    path('lists/',views.list_files_uploaded,name='lists_files'),
  
] 

