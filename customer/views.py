from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	print(request)
	return render(request, 'admin/index.html')
