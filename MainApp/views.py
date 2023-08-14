from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

@login_required(login_url="login")
def data_visualization_view(request):
    # render(request, 'MainApp/data_visualization.html');
    return render(request, 'data_visualization.html')


@login_required(login_url="login")
def Workers_managment_view(request):
    users = User.objects.all()
    groups = Group.objects.all()
    context = {'groups': groups ,'users':users}
    return render(request,'workers_managment.html',context)
@login_required(login_url="login")



def Workers_managment_edit_view(request, pk):
    user = get_object_or_404(User, id=pk)
    groups = Group.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        new_password = request.POST['password']
        new_group_name = request.POST['role']

        # Update user's information
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name

        if new_password:
            user.set_password(new_password)  # Update password if provided

        user.save()

        # Remove user from old groups
        user.groups.clear()

        # Add user to the new group
        new_group = Group.objects.get(name=new_group_name)
        user.groups.add(new_group)

        messages.success(request, 'User data updated successfully.')
        return redirect('workers_managment')

    context = {'user': user, 'groups': groups}
    return render(request, 'workerEdit.html', context)


def delete_users(request):
    if request.method == 'POST':
        user_ids_to_delete = request.GET.get('users', '').split(',')

        # Perform the actual deletion of users
        User.objects.filter(id__in=user_ids_to_delete).delete()

    return redirect('workers_managment')  # Redirect to the workers management page




def add_employee(request):
    if request.method == 'POST':
        # Extract data from the form
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        role = request.POST['role']  # Assuming 'role' is the name of the <select> element
        
        # Create the new user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        
        # Add the user to the selected group
        group = Group.objects.get(name=role)
        user.groups.add(group)
        
        return redirect('workers_managment')  # Redirect to the workers management page
    
    # If the request method is GET, render the workers_managment.html template
    groups = Group.objects.all()
    context = {'groups': groups}
    return render(request, 'workers_managment.html', context)

def delete_user(request, pk):
    user = get_object_or_404(User, id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('workers_managment')
    # If the request method is not POST, return a simple response
    return HttpResponse("Method Not Allowed", status=405)



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
    