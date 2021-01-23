from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from myApp.forms import SignupForm
def home(request):
    return render(request,'myApp/home.html')
@login_required
def java(request):
    return render(request,'myApp/java.html')
@login_required
def python(request):
    return render(request,'myApp/python.html')
@login_required
def apti(request):
    return render(request,'myApp/apti.html')
def logout(request):
    return render(request,'myApp/logout.html')
def Signup(request):
    f=SignupForm()
    if request.method=='POST':
        f=SignupForm(request.POST)
        user=f.save()
        user.set_password(user.password)
        user.save()
        return redirect("/accounts/login")
    d={'form':f}
    return render(request,'myApp/signup.html',d)