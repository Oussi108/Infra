from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url="login")
def data_visualization_view(request):
    # render(request, 'MainApp/data_visualization.html');
    return render(request, 'data_visualization.html')


@login_required(login_url="login")
def Workers_managment_view(request):
    
    return render(request,'workers_managment.html')



def Login_infra_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try :
            user = User.objects.get(username = username)
        except:
            messages.error(request, "User doesnt exist")

        user = authenticate(request,username=username,password=password)
        if user is not None :
            login(request,user)
            url = reverse('data_visualization')

            return redirect(url)
        else :
            messages.error(request,"user doesnt exist or password is incorrect")
    return render(request,'login_infra.html')


@login_required(login_url="login")
def Upload_view(request):
    messages.error(request, "not working yet")
    return render(request,'Upload.html')
   
def logout_user(request):
    logout(request)
    return redirect("login")
    