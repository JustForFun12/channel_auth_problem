from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
	return render(request, 'app/index.html')

def room(request, group_name):
	return render(request, 'app/index.html')

def login(request):
	form = UserCreationForm()
	return render(request, 'app/login.html', {'form':form})

