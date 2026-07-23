from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def signup(request):
  if request.method=="POST":
    form=SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username=request.POST["username"]
      password=request.POST["password1"]
      user=authenticate(request,username=username,password=password)
      login(request,user)
      redirect("dashboard")
      messages.success(request,"Registered successfully")
    else:
      redirect("signup")
      messages.error(request,"Registration fail")
  else:
    form=SignUpForm()
    return render(request,'register.html',{"form":form})
  
def signin(request):
  
  if request.method=="POST":
    username=request.POST["username"]
    password=request.POST["password"]     
    
    user=authenticate(request,
            username=username,password=password)
    if user is not None:
      login(request,user)
   
      messages.success(request,"Logged in successfully")
      return redirect("dashboard")
    else:
     messages.error(request,"Invalid credentials")
     return redirect("login")
  else:
     return render(request,'login.html')
  
def signout(request):

  logout(request)
  return redirect("login")