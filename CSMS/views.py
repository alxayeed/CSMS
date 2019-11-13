from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
	print(request)
	return render(request, 'index.html')

def loginPage(request):
	return render(request,'loginpage.html')