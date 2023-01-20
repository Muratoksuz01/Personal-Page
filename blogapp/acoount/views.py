from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.

def Login_request(request):
    if request.user.is_authenticated:
        return redirect("HOME")
    if request.method=="POST":#post eildimi diye bakıyor 
        username=request.POST["username"]# bilgileri alıyorum 
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)#burada kişi varmı diye bakıyorum 
        if user is not None:
            login(request,user)
            return redirect("HOME")
        else :
            return render (request,"account/login.html",{
                "error":"username yada parola yanlış"
            })
    return render(request,"account/login.html")


def register_request(request):
    if request.user.is_authenticated:
        return redirect("HOME")
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        password=request.POST["password"]
        repassword=request.POST["repassword"]

        if password==repassword:
            if User.objects.filter(username=username).exists():
                return render(request,"account/register.html",{
                    "error":"kullanıcı mevcut",
                    "email":email,#                         bunlar hata yaptıgında silinmesin diye yazdıkları register.html den yazdıracam bunları 
                    "username":username,
                    "firstname":firstname,
                    "lastname":lastname
                    })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request,"account/register.html",{
                    "error":"email kullaniliyor ",
                    "email":email,
                    "username":username,
                    "firstname":firstname,
                    "lastname":lastname
                    })
                else:
                    user=User.objects.create_user(username=username,email=email,password=password,
                    first_name=firstname,last_name=lastname)
                    user.save()
                    return redirect("Login")

        else:
            return render(request,"account/register.html",{
                "error":"parolalar eşleşmiyor",
                    "email":email,
                    "username":username,
                    "firstname":firstname,
                    "lastname":lastname
                    })







    return render(request,"account/register.html")


def Logout_request(request):
    logout(request)
    return redirect("HOME")