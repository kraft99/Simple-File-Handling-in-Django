from django.shortcuts import render
import os
from django.http import HttpResponse, Http404, StreamingHttpResponse, FileResponse
from upload.models import UploadFile

# Good for .txt,not suitable for big binary files
# def file_download(request,file_path):
# 	with open(file_path,'rb') as file:
# 		try:
# 			response = HttpResponse(file)
# 			response['content_type'] = 'application/octet-stream'
# 			response['Content-Disposition'] = 'attachment; filename='+os.path.basename(file_path)
# 			return response
# 		except Exception:
# 			raise Http404



# def file_download(request,file_path):
# 	'''
# 	uses StreamingHttpResponse to download a large file.
# 	Good for streaming large binary files ie.CSV files
#   Do not support python file "with" context manager - handle. Consumes response time
# 	'''
# 	try:
# 		response = StreamingHttpResponse(open(file_path,'rb'))
# 		response['content_type'] = 'application/octet-stream'
# 		response['Content-Disposition'] = 'attachment; filename='+os.path.basename(file_path)
# 		return response
# 	except Exception:
# 		raise Http404



def file_download(request,file_path):
	'''
	uses FileResponse to download a large file.
	It streams the file out in small chunks
	The file will be closed automatically, so don’t open it with a context manager (with - statement ).
	'''
	
	try:
		response = FileResponse(open(file_path,'rb'),as_attachment=False,filename='')#read docs.
		response['content_type'] = 'application/octet-stream'
		response['Content-Disposition'] = 'attachment; filename='+os.path.basename(file_path)
		return response
	except Exception:
		raise Http404
