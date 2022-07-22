from telnetlib import STATUS
from django.shortcuts import render,redirect
from .models import Category,Course, Video,User
from .forms import CardForm,PaymentForm
from django.contrib import messages
from django.db.models import Prefetch
from account.forms import LoginForm, RegistrationForm
# Create your views here.


def main_index(request):    
    
    return render(request, "main/index.html",{
        'category': Category.objects.all(),
        'course': Course.objects.all(),
        'video':Video.objects.filter(status=1)
    })


def category(request):
    pass

def course(request,pk):


    course = Course.objects.filter(id=pk)
    video = []
    
    for res in Video.objects.filter(course_id=pk):
        
        if res.status == 1:
            video.append(res.video)
            
   
    
    
    
    return render(request,'main/courses-details.html',{
            'course_id':course,
            'video':video
            
        })

def payment(request,pk):
    course = Course.objects.filter(id=pk)
    form = PaymentForm()
    if request.method == "POST":
        form=PaymentForm(data=request.POST)     
        if form.is_valid() and request.user.is_staff:
             
               form.save()  
               messages.success(request,("Payment successfully done,learn this course and enjoy with us!"))
               return redirect("main:courses",pk)           
        else:
               messages.warning(request,("Payment has not been done,please add your card"))
               return redirect("main:payment",pk) 
            
                             
                
    return render(request,'payment/payment.html',{
        'form':form,
        "card":course
    })   
        
  

def create_card(request,pk): 
    form = CardForm()
    
    if request.method == "POST":
        form=CardForm(data=request.POST)        
        if form.is_valid():                       
            if not request.user.is_staff:
                request.user.is_staff = True
                request.user.save()
                
            form.save()

            messages.success(request,("Card successfully added"))
            return redirect("main:payment",pk)           

    return render(request, "payment/card.html",{
        "form": form,        
    })

def courses_page(request,pk):
    videos = Video.objects.filter(course_id=pk)
    return render(request,'main/courses.html',{
        'courses':videos
    })


def handle_not_found(request,exception):
    return render(request,'main/error-404.html')

    