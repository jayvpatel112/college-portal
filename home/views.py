from django.shortcuts import render, redirect, HttpResponse
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate, login, logout
from django.contrib import messages
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.
def home(request):
    # return HttpResponse('this is home')
    return render(request, 'home/home.html')

def contact(request):
    # messages.success(request, "Your message has been successfully sent")
    # messages.error(request, "Your message has been successfully sent")
    if request.method=='POST':
        # print('We are using post request')
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, 'Plese fill the form correctly')
        else :
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'your message has been successfully sent')
    return render(request, 'home/contact.html')
    # return HttpResponse('this is contact')

@csrf_exempt
def handleSignUp(request):
    if request.method=="POST" :
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        try :
            # check for errorneous input
            if len(username)>10:
                messages.error(request, " Your user name must be under 10 characters")
                return redirect('home')

            if not username.isalnum():
                messages.error(request, " User name should only contain letters and numbers")
                return redirect('home')
            if (pass1!= pass2):
                messages.error(request, " Passwords do not match")
                return redirect('home')

            if User.objects.filter(username = username):
                messages.success(request, " Username is already used by another user, please choose another username.")
                return redirect('home')

            if User.objects.filter(email = email):
                messages.success(request, " Email is already exist.")
                return redirect('home')

                # Create the user
            myuser = User.objects.create(username = username, email = email)
            myuser.set_password(pass1)
            myuser.first_name= fname
            myuser.last_name= lname
            myuser.save()

            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user=myuser , auth_token = auth_token)
            profile_obj.save()

            messages.success(request, " We have sent an email to you    Please check your email")
            send_after_signup(email, auth_token)        
            return redirect('home')
            
        except Exception as e:
            print(e)
    
    # else:
    #     return HttpResponse("404 - Not found")


def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        
        user_obj = User.objects.filter(username = loginusername).first()
        if user_obj is None:
            messages.error(request, " User not found. ")
            return redirect("home") 

        profile_obj = Profile.objects.filter(user = user_obj).first()
        if not profile_obj.is_verified:
            messages.error(request, " Profile is not verified check your mail. ")
            return redirect("home")


        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


# def token_send(request):
#     return render(request, 'home/token_send.html')

def success(request):
    return render(request, 'home/success.html')


def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
        if profile_obj :
            if profile_obj.is_verified:
                messages.success(request, "    your account is already verified")
                return redirect("home")
            
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, "    your account has been verified       Login")
            return redirect("home")
        else:
            return redirect("error")
    except Exception as e:
        print(e)


def error_page(request):
    return render(request, 'home/error.html')


def send_after_signup(email, token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your accout http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)