from django import forms
from .models import UploadFile



class UploadFileForm(forms.ModelForm):
	
	class Meta:
		model = UploadFile
		fields = ['image']




class UploadRawFile(forms.Form):
	upload = forms.FileField(help_text='format supported are jpg,jpeg,png.')