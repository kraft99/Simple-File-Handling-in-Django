import os
import uuid
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UploadFileForm,UploadRawFile
from .models import UploadFile
from django.conf import settings



def list_files_uploaded(request):
	files = UploadFile.objects.all()
	return render(request,'files_lists.html',{'files':files})




def upload_view(request):
	if request.method == 'POST':
		form = UploadFileForm(data = request.POST,files = request.FILES)
		if form.is_valid():
			print("valid form")
			upload_instance = form.save(commit=False)
			upload_instance.save()
			return HttpResponse("File uploaded successfully")
		else:
			print("Invalid form")

	print("Get request")
	form = UploadFileForm()
	context = {
	'upload_form':form
	}
	return render(request,'uploads.html',context)






def upload_raw_file(request):
	if request.method == 'POST':
		form = UploadRawFile(data = request.POST,files = request.FILES)
		if form.is_valid():
			file = form.cleaned_data['upload']
			if is_correct_file_format(file):
				file_instance = UploadFile()
				# file_instance.image = handle_uploaded_file(file)
				file_instance.image = file
				file_instance.save()
				return HttpResponse("successfully uploaded file")
			else:
				return HttpResponse("wrong format")
		return HttpResponse('failed to upload file')
	form  = UploadRawFile()
	c = {
	'form':form
	}
	return render(request,'upload_file.html',c)


# Scripts checks file format before commiting to database Model
def is_correct_file_format(instance):
	instance_ext = instance.name.split('.')[-1].lower()
	if not instance_ext in settings.FILE_VALIDATION_EXTENSIONS:
		return False
	return True







# "isinstance(obj,[int,float,str])"



# def handle_uploaded_file(file):
#     ext = file.name.split('.')[-1]
#     file_name = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
#     # file path relative to 'media' folder
#     file_path = os.path.join('images', file_name)
#     absolute_file_path = os.path.join('media', 'images', file_name)

#     directory = os.path.dirname(absolute_file_path)
#     if not os.path.exists(directory):
#         os.makedirs(directory)

#     with open(absolute_file_path, 'wb+') as destination:
#         for chunk in file.chunks():
#             destination.write(chunk)

#     return file_path