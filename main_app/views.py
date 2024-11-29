from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.

akhbar=Akhbar.objects.all()
info=Info.objects.all()
shahrie=Shahrie_1.objects.all()


def home(request):
    return render(request,"main_app/index-3.html",context={'akhbar':akhbar,'info':info})

def blog(request):
    return render(request,"main_app/blog.html",context={'akhbar':akhbar,'info':info})

def bmi(request):
    return render(request,"main_app/bmi-calculator.html",context={'akhbar':akhbar,'info':info})

def test(request):
    sk=request.POST.get("skey")
    if(sk):
        usr=Akhbar.objects.filter(title__contains=sk)
        return render(request,"main_app/test.html",context={'akhbar':akhbar,'info':info,"search":usr})

    return render(request,"main_app/test.html",context={'akhbar':akhbar,'info':info})

def success(request):
    return render(request,"main_app/success.html",context={'akhbar':akhbar,'info':info})

def contact(request):
    f=ContactForm()
    if(request.method=="POST"):
        f=ContactForm(request.POST)
        if f.is_valid():
            n=f.cleaned_data["n"]
            e=f.cleaned_data["e"]
            p=f.cleaned_data["p"]
            t=f.cleaned_data["t"]
            m=f.cleaned_data["m"]
            Contact.objects.create(name=n,email=e,phone_number=p,title=t,message=m)

            return redirect("/success")
            

    return render(request,"main_app/contact.html",context={'akhbar':akhbar,'info':info,"f":f})

def khabar1(request):
    return render(request,"main_app/Khabar1.html",context={'akhbar':akhbar,'info':info})

def khabar2(request):
    return render(request,"main_app/Khabar2.html",context={'akhbar':akhbar,'info':info})

def khabar3(request):
    return render(request,"main_app/Khabar3.html",context={'akhbar':akhbar,'info':info})

def khabar4(request):
    return render(request,"main_app/Khabar4.html",context={'akhbar':akhbar,'info':info})

def khabar5(request):
    return render(request,"main_app/Khabar5.html",context={'akhbar':akhbar,'info':info})

def khabar6(request):
    return render(request,"main_app/Khabar6.html",context={'akhbar':akhbar,'info':info})

def khabar7(request):
    return render(request,"main_app/Khabar7.html",context={'akhbar':akhbar,'info':info})

def Shahrie(request):
    return render(request,"main_app/shahrie.html",context={'akhbar':akhbar,'info':info,'shahrie':shahrie})

def about(request):
    return render(request,"main_app/about.html",context={'akhbar':akhbar,'info':info})

def layout(request):
    return render(request,"main_app/layout.html",context={'akhbar':akhbar,'info':info})

def detailLayout(request):
    return render(request,"main_app/detail khabar layout.html",context={'akhbar':akhbar,'info':info})