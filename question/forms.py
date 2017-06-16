from django import forms 
from django.contrib.auth.models import User 
from .models import Question,Answer




class SignUpForm(forms.ModelForm):
	username = forms.CharField(widget = forms.TextInput(attrs = {'class':'form-control'}), 
		max_length = 20,
		required= True
		)
	password = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'form-control'}),
		min_length = 6,
		required =True)
	confirm_password = forms.CharField(widget = forms.PasswordInput(attrs= {'class':'form-control'}),
		label = "confirm your password",
		required = True )
	email = forms.CharField(widget = forms.EmailInput(attrs={'class':'form-control'}),
		required = True )
	class Meta:
		model =User
		exclude =['last_login','date_joined']
		fields = ['username','password','confirm_password','email',]

	def clean(self):
		cleaned_data = super(SignUpForm,self).clean()
		password = cleaned_data.get('password')
		confirm_password= cleaned_data.get('confirm_password')
		if password and password != confirm_password:
			msg = "Passwords do not match"
			self.add_error('confirm_password',msg)

class QuestionForm(forms.ModelForm):
	title = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control'}),
		min_length =10,
		required = True)
	description = forms.CharField(widget=forms.Textarea(attrs= {'class':'form-control'}),
		min_length =10,
		required= True)
	tags = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control'}),
		min_length = 6,
		required =True,
		help_text='Entering tags helps to order the question for people interested in the particular tag')
	class Meta:
		model = Question
		fields =['title','description','tags',]

class AnswerForm(forms.ModelForm):

	question = forms.ModelChoiceField(widget=forms.HiddenInput(),
                                      queryset=Question.objects.all())
	description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),max_length=2000)

	class Meta:
		model = Answer
		fields = ['description']







