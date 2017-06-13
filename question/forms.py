from django import forms 
from django.contrib.auth.models import User 






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
