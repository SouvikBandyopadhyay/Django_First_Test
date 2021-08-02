from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth


# Create your views here.
def addaccount(request):

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        user_name=request.POST['user_id']
        email=request.POST['email']
        password1=request.POST['pass1']
        password2=request.POST['pass2']

        if password1!=password2:
            messages.info(request,'Password not matching')
            return redirect('register')
        elif User.objects.filter(username=user_name).exists():
            messages.info(request,'username taken')            
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email taken')
            return redirect('register')
        else:

            user=User.objects.create_user(username=user_name,password=password1,email=email,first_name=first_name,last_name=last_name)
            user.save()
            print("user created")
            return redirect('login')
        
    else:
        return render(request,'register.html')

def enteraccount(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("exits")
            return redirect("/")
        else:
            messages.info(request, "Bad Cred")
            return redirect('login')


    return render(request,'login.html')

def exitaccount(request):
    auth.logout(request)
    return redirect('/')