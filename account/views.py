from django.shortcuts import render,redirect
from .forms import RegistrationForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def account_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = username, password = password)
            if user is not None:
                login(request,user)
                messages.success(request, ("Welcome {},now you can book your room!".format(user.username)))        
                return redirect('main:index')
            form.add_error('password',("Login or password is not true"))
    return render(request,"account/login.html",{
        'form' : form
    })


def account_register(request):
    form=RegistrationForm()
    if request.method=='POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.instance.set_password(form.cleaned_data.get('password'))
            # form.instance.is_active=False
            form.save()

            messages.success(request,("Successfully registered"))
            return redirect("account:login")

            
    return render(request,'account/register.html',{
        'form':form
    })


def account_logout(request):
    
    logout(request)    
    
    messages.success(request, "Goodbye!")         
    return redirect('main:index')


def forget_password(request):
    return render(request, "account/forget-password.html")


def membership(request):
    return render(request, "account/membership.html")


def profile(request):
    return render(request, "account/profile.html")


def portfolio(request):
    return render(request, "account/portfolio.html")
