from django.shortcuts import render
from app.forms import *
from app.models import *
# Create your views here.
def home(request):
    return render(request,'home.html',)


def register(request):
    form=CompanyForm()
    d={'form':form}
    if request.method=='POST':
        form_data=CompanyForm(request.POST)
        if form_data.is_valid():
            m=form_data.cleaned_data['mobile']
            p=form_data.cleaned_data['password']
            cp=form_data.cleaned_data['confirmpassword']
            obj=MYC.objects.get_or_create(mobile=m,password=p,confirmpassword=cp)[0]
            obj.save()
    return render(request,'register.html',d)

def login(request):
    return render(request,'login.html')

def company(request):
    return render(request,'company.html')