
from django.shortcuts import redirect, render
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.contrib.auth.models import User
from django.contrib import messages , auth
from.models import Product
# Create your views here.
def fun(request):
    products_list=None
    products_list=Product.objects.all()
    paginator=Paginator(products_list,3)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
    return render(request,'index.html',{'products':products})
def about(request):
    return render(request,'about.html')
def furniture(request):
    return render(request,'furniture.html')
def blog(request):
    return render(request,'blog.html')
def contact(request):
    return render(request,'contact.html')
def loginform(request):
    if request.method=='POST':
        usernamelog=request.POST['usernamelogin']
        passwordlog=request.POST['passwordlogin']
        userdb=auth.authenticate(username=usernamelog,password=passwordlog)
        if userdb is not None:
            auth.login(request,userdb)
            return redirect('edgecutapp:fun')
        else:
            print('error')
            return redirect('edgecutapp:loginform')
    return render(request,'loginform.html')

def login(request):
    if request.method=='POST':
        username1=request.POST['username']
        firstname1=request.POST['firstname']
        lastname1=request.POST['lastname']
        email1=request.POST['email']
        password1=request.POST['password']
        cpassword1=request.POST['cpassword']
        if password1==cpassword1:
            if User.objects.filter(username=username1).exists():
                messages.info(request,'Username already taken.')
                print('username already taken')
                return redirect('/')
            else:
                user=User.objects.create_user(username=username1,first_name=firstname1,last_name=lastname1,email=email1,password=password1)
                user.save()
                return redirect('edgecutapp:loginform')
        else:        
            return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')