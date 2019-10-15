from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
	print(request)
	return render(request, 'index.html')

def sign_up(request):
	form = UserCreationForm()
	return render(request,'sign_up.html',{'signup_form':form})