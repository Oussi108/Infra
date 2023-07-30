from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def data_visualization_view(request):
    # render(request, 'MainApp/data_visualization.html');
    return render(request, 'data_visualization.html')
def Workers_managment_view(request):
    
    return render(request,'workers_managment.html')
def Login_infra_view(request):
    
    return render(request,'login_infra.html')
def Upload_view(request):
    return render(request,'Upload.html')