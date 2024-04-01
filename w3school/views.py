from django.shortcuts import render
from django.http import JsonResponse
from .models import  Customers

# Create your views here.
def home(request):

    return render(request,"home.html",{"data":Customers.objects.all()})

def test(request):
    data=Customers.objects.all().values()
    return JsonResponse({'data' : list(data)}) #safe=False
