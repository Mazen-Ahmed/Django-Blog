from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .form import registrationform
from django.contrib.auth.models import User
from article.models import article

def registeration(request):
    if request.method=='GET':
        form=registrationform()
    else:
        form=registrationform(request.POST)
        if form.is_valid():
            form.save()
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            login(request,user)
            return redirect('/articles/')
    return render(request,'register.html',{'form':form})

def LogIn(request):
     if request.method=='POST':

        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/articles/')
     else:
        form=AuthenticationForm()
     return render(request,'login.html',{'form':form})
def logOut(request):
        logout(request)
        return redirect('/articles/')

def Profile(request):
    x=article.objects.all()
    return render(request,'profile1.html',{'x':x})


def userprofile(request,id):
    us=User.objects.get(id=id)
    x=article.objects.filter(User=id)
    return render(request,'profile2.html',{'us':us,'x':x})