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


class Question(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length = 100)
	description = models.TextField(max_length = 500)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	favorites = models.IntegerField(default= 0)
	accepted_answer = models.BooleanField(default= False)

	class Meta:
		verbose_name='Question'
		verbose_name_plural ='Questions'
		ordering =('-updated_at','-created_at',)

	def __str__(self):
		return self.title 

	def create_tags(self, tags):
		tags= tags.strip()
		tag_list = tags.split(' ')
		for tag in tag_list:
			 t, created = Tag.objects.get_or_create(tag=tag.lower(), question=self)


class Answer(models.Model):
 	user = models.ForeignKey(User)
 	question = models.ForeignKey(Question)
 	description= models.TextField(max_length= 2000)
 	created_at = models.DateTimeField(auto_now_add=True)
 	updated_at =models.DateTimeField(auto_now_add=True)
 	is_accepted = models.BooleanField(default = 0)
 	votes = models.IntegerField(default =0)

 	class Meta:
 		verbose_name='Answer '
 		verbose_name_plural='Answers'
 		ordering =('-votes','-is_accepted','-created_at',)

 	def __str__(self):
 		return self.description

class Tag(models.Model):
    tag = models.CharField(max_length=50)
    question = models.ForeignKey(Question)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        unique_together = (('tag', 'question'),)
        index_together = [['tag', 'question'], ]

    def __str__(self):
        return self.tag



    