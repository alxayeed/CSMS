from django.shortcuts import render
from .models import Area,Employe
from django.db import connection

# Create your views here.
def index(request):
	return render(request,'employe/index.html')

def login(request):
	if request.method == 'POST':
		with connection.cursor() as cursor:
			email = request.POST.get('email')
			password = request.POST.get('password')
			print(email,password)
		   
			try:
				if Employe.objects.get(email=email):
					cursor.execute("select * from employe_employe where email = %s", [email]) 
					is_user = cursor.fetchone()
					print('this is',is_user)
					

					if  password != is_user[5] :
						message = 'Password incorrect!'
						return render(request,'employe/login.html',{'context':message })

					else :
						request.session['user'] = is_user #logged in users data is assigned to a variable
						message = 'Welcome '+is_user[4]
						user = is_user[4]
						
						return render(request,'employe/index.html',{'context':message,'user':user })
			except Exception as e:
					print('THE ERROR IS ',e)
					message = 'Email not found!'
					return render(request,'employe/login.html',{'context':message })
	return render(request,'employe/login.html')




def logout(request):
	pass

def viewProfile(request):
	pass

def updateProfile(request):
	pass

def viewOrderList(request):
	pass

def viewOrderDetails(request):
	pass

def orderConfirmation(request):
	pass