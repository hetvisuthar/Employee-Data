from django.shortcuts import render
from .models import employees
from django.contrib import messages
from pymsgbox import *
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):

    if employees.objects.exists():
        emp_Det = employees.objects.all().values('employee_ID','employee_name','designation','address','phone_num')
    else:
        emp_Det = "No Applications Yet!!"
        
    print(emp_Det)
    return render(request,'first_app.html',{'emp_Det':emp_Det})

def add(request):
    if request.method == 'POST':
        employee_ID = request.POST['employee_ID']
        employee_name = request.POST['employee_name']
        designation = request.POST['designation']
        address = request.POST['address']
        phone_num = request.POST['phone_num']
        if employees.objects.filter(employee_ID = employee_ID).exists():
            messages.info(request,'Employee_ID Already Exists')
            alert(text='', title='Employee_ID Already Exists')
        
        else:
            alert(text='', title='Employee Details Added Successfully')      
            storeInTable = employees(employee_ID=employee_ID,employee_name=employee_name,designation=designation,address=address,phone_num=phone_num)
            storeInTable.save()

        return redirect('home')
    return render(request,'first_app.html')

def delete(request):  
    if request.method == 'POST':
        ID = request.POST['ID']
        
        print("\nID :",ID)
        employees.objects.get(employee_ID=ID).delete()
        alert(text='', title='successfully Deleted')    
    return render(request,'first_app.html')
