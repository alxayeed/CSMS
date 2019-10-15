from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def customer_index(request):
	return render(request, 'customer/customeri.html')
