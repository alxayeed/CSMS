from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.db import connection
# from .forms import UserRegistrationForm

# Create your views here.
def customer_index(request):
	return render(request, 'customer/base.html')

def customer_signup(request):
	if request.method == 'POST':
		with connection.cursor() as cursor:
			first_name = request.POST.get('firstname')
			last_name = request.POST.get('lastname')
			email = request.POST.get('email')
			password = request.POST.get('password1')
			password2 = request.POST.get('password2')
			
			try :
				if User.objects.get(email=email):
					message = 'Email Already exists!'
					return render(request,'sign_up.html',{'context':message })
			except Exception as e:
				pass

			if password != password2:
				message = 'Paasword Missmatched!'
				return render(request,'sign_up.html',{'context':message })
			elif len(password)<8:
				message = 'Paasword should be at least 8 character'
				return render(request,'sign_up.html',{'context':message })

			else:
				u = User(first_name=first_name,last_name=last_name,email=email,password=password)
				u.save()
				message = 'Data Saved Successfully'
				return render(request,'customer/login.html',{'context':message })

	return render(request,'sign_up.html')


def customer_login(request):
	if request.method == 'POST':

		with connection.cursor() as cursor:
			email = request.POST.get('email')
			password = request.POST.get('password')

			try:
				if User.objects.get(email=email):
					is_user = User.objects.get(email=email)

					if  password != is_user.password:
						message = 'Password incorrect!'
						return render(request,'customer/login.html',{'context':message })

					else :
						message = 'Congo!'
						return render(request,'customer/index.html',{'context':message })
			except Exception as e:
					message = 'Email not found!'
					return render(request,'customer/login.html',{'context':message })
	return render(request,'customer/login.html')


def customer_logout(request):
	print(request.session)
	session = request.session
	if session:
		del session
		message = 'Successfully logged out'
		return render(request,'customer/login.html',{'context':message })


	return render(request,'customer/index.html',{"context":session})
