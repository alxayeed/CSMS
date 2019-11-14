from django.shortcuts import render
from .models import Area,Employe
from customer.models import Order 	
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
	message = 'Successfully logged out'
	session = request.session['user']
	if session:
		del session
		message = 'Successfully logged out'
		return render(request,'employe/login.html',{'context':message })
	else:
		message = 'You haven\'t logged in yet'
		return render(request,'employe/login.html',{'context':message })



	return render(request,'employe/index.html')

def viewProfile(request):
	pass

def updateProfile(request):
	pass

def viewOrderList(request):
	logged_user = request.session['user']
	print(logged_user)
	profile_name  = logged_user[4]
	work_area = logged_user[1]
	

	order_list = Order.objects.all().filter(order_area=work_area)
	print(order_list)

	return render(request,'employe/order_list.html',{'order_list':order_list,'user':profile_name})

def viewOrderDetails(request,order_id):
	logged_user = request.session['user']
	profile_name  = logged_user[4]

	if request.method == 'GET':
		logged_user = request.session['user']
		order_by = logged_user[1]

		order = Order.objects.get(pk = order_id)

		
	return render(request,'employe/view_order.html',{'context':order,'user':profile_name})

def orderConfirmation(request):
	pass