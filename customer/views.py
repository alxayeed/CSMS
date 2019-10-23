from django.shortcuts import render,redirect
from .models import User,Order
from django.db import connection


# Create your views here.
def customer_index(request):
    return render(request, 'customer/index.html')

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
            # user = authenticate(request,email=email, password=password)


            try:
                if User.objects.get(email=email):
                    cursor.execute("select * from customer_user where email = %s", [email]) 
                    is_user = cursor.fetchone()
                    print('this is',is_user)

                    if  password != is_user[4] :
                        message = 'Password incorrect!'
                        return render(request,'customer/login.html',{'context':message })

                    else :
                        request.session['user'] = is_user #logged in users data is assigned to a variable
                        message = 'Congo '+is_user[1]
                        user = is_user[1]+' '+is_user[2]
                        
                        return render(request,'customer/index.html',{'context':message,'user':user })
            except Exception as e:
                    print('THE ERROR IS ',e)
                    message = 'Email not found!'
                    return render(request,'customer/login.html',{'context':message })
    return render(request,'customer/login.html')


def customer_logout(request):
    message = 'Successfully logged out'
    session = request.session['user']
    print(session)
    if session:
        print(session)
        del session
        message = 'Successfully logged out'
        return render(request,'customer/login.html',{'context':message })
    else:
        message = 'You haven\'t logged in yet'
        return render(request,'customer/login.html',{'context':message })



    return render(request,'customer/index.html')


def profile(request):
    logged_user = request.session['user']
    profile_name  = logged_user[1]+' '+logged_user[2]
    
    return render(request,'customer/profile.html',{'user':profile_name,'logged_user':logged_user })

def update_profile(request):
    logged_user = request.session['user']
    u = User.objects.get(email=logged_user[3])
    print(u.first_name,request.method)
    if request.method == 'GET':
        profile_name  = u.first_name+' '+u.last_name

        return render(request,'customer/update_profile.html',{'user':profile_name,'logged_user':logged_user})

    if request.method == 'POST':
        if request.POST.get('firstname'):
            u.first_name = request.POST.get('firstname')
        else :
            u.first_name 
        if request.POST.get('lastname'):
            u.last_name = request.POST.get('lastname')
        else :
            u.last_name
        if request.POST.get('email'):
            u.email = request.POST.get('email')
        else :
            u.email

        u.save()

    return render(request,'customer/profile.html')


def make_order(request):
    logged_user = request.session['user']
    u = User.objects.get(email=logged_user[3])
    profile_name  = u.first_name+' '+u.last_name

    if request.method == 'GET':
        return render(request,'customer/make_order.html',{'user':profile_name })

    if request.method == 'POST':
        sender_name = request.POST.get('sender_name')
        sender_contact = request.POST.get('sender_contact')
        sender_address = request.POST.get('sender_address')
        reciever_name = request.POST.get('reciever_name')
        reciever_contact = request.POST.get('reciever_contact')
        reciever_address = request.POST.get('reciever_address')
        quantity = request.POST.get('product_quantity')
        shipment_cost = 50

        order = Order(sender_name = sender_name,
        sender_contact=sender_contact,
        sender_address = sender_address,
        reciever_name = reciever_name,
        reciever_contact = reciever_contact,
        reciever_address = reciever_address,
        product_quantity = quantity,shipment_cost=shipment_cost)


        order.save()
        order = Order.objects.get(sender_name=sender_name)
        
        



    return render(request,'customer/order_details.html',{'order':order,'user':profile_name})

def view_order(request):
    pass


def order_details(request):
    pass



