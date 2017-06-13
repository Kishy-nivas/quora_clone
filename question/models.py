from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
 
class userprofile(models.Model):
	user = models.OneToOneField(User)
	college_studied = models.CharField(max_length = 50, null = True ,blank = True)
	location = models.CharField(max_length =20, null = True, blank = True )
	bio = models.TextField(max_length = 75, null = True,blank = True)


	class Meta:
		verbose_name='userprofile'

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		self

    
def create_userprofile(sender ,**kwargs):
	user = kwargs["instance"]
	if kwargs["created"]:
		user_profile = userprofile(user=user )
		user_profile.save()

post_save.connect(create_userprofile,sender= User)

    