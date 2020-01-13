from django.db import models
from django.conf import settings
import uuid
import os




def upload_location(instanse,file_obj):
	file_ext = file_obj.split('.')[-1]
	file_obj = '{}.{}'.format(uuid.uuid4().hex[:10],file_ext)
	return os.path.join("images",file_obj)
	# PATH:media/images/file_name


# def upload_user_dir_loc(instanse,file_obj):
# 	return 'user_{0}/{1}'.format(instanse.user.id,file_obj)
# 	# PATH:media/user_id_number/user_file


def upload_unique_loc(instanse,file_obj):
	file_ext = file_obj.split('.')[-1]
	file_obj = '{}.{}'.format(uuid.uuid4().hex[:8],file_ext)
	return os.path.join('user_media',str(instanse.user.username),'images',file_obj)
	# PATH : media/user_media/user_username/images/file_name
	# Eg. : media/user_media/admin/images/family_pic.png






class UploadFile(models.Model):
	image     = models.FileField(upload_to=upload_unique_loc,default=None,blank=True,null=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True,on_delete=models.CASCADE,default=1)

	def __str__(self):
		return str(self.image)


	@property
	def get_file_url(self):
		return self.image.url if self.image.url else ""
		# url = self.image.url
		# return url
