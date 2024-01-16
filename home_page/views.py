from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import Product,Customer,Cart,OrderPlace
from django.views import View
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash



# Create your views here.
def home(request):
    return render(request, 'main/base.html')

class ProductView(View):
    def get(self,request):
        jeans = Product.objects.filter(category='JP')
        laptop = Product.objects.filter(category='LP')
        justfor = Product.objects.filter(category='JF')
        electic = Product.objects.filter(category='EL')

        return render(request,'main/jeans.html',{'jeanspants':jeans,'laptop':laptop,'electic':electic,'justfor':justfor})

class ProductDetalisView(View):
      def get(self,request,pk):
           productview = Product.objects.get(pk=pk)
           return render(request,'main/productview.html',{'productview':productview})
class LehengaView(View):
     def get(self,request):
        lehenga = Product.objects.filter(category='LE')
        return render(request,'main/lehenga.html',{'lehenga':lehenga,})
class BorkhaView(View):
     def get(self,request):
        borkha = Product.objects.filter(category='BO')
        return render(request,'main/borkha.html',{'borkha':borkha,})
class TshirtView(View):
      def get(self,request):
           tshirt = Product.objects.filter(category='TS')
           return render(request,'main/tshirt.html',{'tshirt':tshirt})

class ShirtDetalisView(View):
      def get(self,request,pk):
           shirtview = Product.objects.get(pk=pk)
           return render(request,'main/shirtview.html',{'shirtview':shirtview})
class BoyShirtView(View):
      def get(self,request):
           boys = Product.objects.filter(category='BS')
           return render(request,'main/boyshirt.html',{'boyshirt':boys})
class WinterView(View):
      def get(self,request):
           winter = Product.objects.filter(category='WD')
           return render(request,'main/winter.html',{'winters':winter})

class PhoneView(View):
      def get(self,request):
           phone = Product.objects.filter(category='PH')
           return render(request,'main/phone.html',{'phone':phone})
# Create UserCreation Form views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            form.save
            messages.success(request, 'Wellcome Dashboard')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
        return render(request, 'main/createform.html',{'registers': form})

# Create Authenticatedform views here.
def loginview(request):
     if request.method=='POST':
          lgin = AuthenticationForm(request=request,data=request.POST)
          if lgin.is_valid():
           username = lgin.cleaned_data.get['username']
           password = lgin.cleaned_data.get['password1']
           user = authenticate(request,username=username, password1=password)
           if user is not None:
                login(request,user)
                return redirect('/home/')
     
     else:
      lgin = AuthenticationForm()
     return render(request,'main/login.html',{'login':lgin})
def logouts(request):
    logout(request)
    return HttpResponseRedirect('/login/')