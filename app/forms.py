from django import forms
from django.contrib.auth.models import User
# wow! just found out we don't even need this!!!! hahahahaahahahaahahahahaha!!!!!!!!!!!!!

class CustomForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']