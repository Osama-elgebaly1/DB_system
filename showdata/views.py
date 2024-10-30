from django.shortcuts import render,redirect
from .models import Customer
from django.http import HttpResponse
# Create your views here.

def home(request):
    customers = Customer.objects.all()
    return render(request,'home.html',{'customers':customers})


def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
       

        new = Customer(name=name,age=age,email=email)
        new.save()
        return redirect('/')

    
    else:
        return render(request,'add.html',{})

    

def update(request,id):
    customer = Customer.objects.get(id=id)
    if request.method == 'POST':
        customer.name = request.POST['name']
        customer.age = request.POST['age']
        customer.email = request.POST['email']

        customer.save()
        return redirect('/')
    else:
        return render(request,'update.html',{'customer':customer})


def delete(request,id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect('/')
