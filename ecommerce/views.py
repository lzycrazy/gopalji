from django.shortcuts import render,redirect
from django.contrib import messages
from.models import *
from django.contrib.auth import authenticate,login,logout


# Create your views here.



def index(request):
    carausel=Carausel.objects.all()
    categary=Categary.objects.all()
    products=Products.objects.all()
    about=About.objects.all()
    latest = Products.objects.order_by('price')[0:8]
    context={
        'cara':carausel,
        'pro':products,
        'cat':categary,
        'about':about,
        'item':latest,

        }
    return render(request,'index.html', context)

def about(request):
    about=About.objects.all()
    categary=Categary.objects.all()

    context={
        'cat':categary,
        'about':about,

        }
    return render(request,'about.html', context)

def product(request):
    products=Products.objects.all()
    categary=Categary.objects.all()
    context={
        'cat':categary,
        'pro':products
        }
    return render(request,'product.html',context)  

def contact(request):
    return render(request,'contact.html') 

def why(request):
    categary=Categary.objects.all()

    context={
        'cat':categary

        }
    return render(request,'why.html',context)

def categary(request,slug):
    carausel=Carausel.objects.all()
    categary=Categary.objects.all()
    cat=Categary.objects.get(slug=slug)
    products=Products.objects.filter(categary=cat)
    

    context={
        'cara':carausel,
        'pro':products,
        'cat':categary,
        }
    return render(request,'product.html', context)   


def contact(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<5:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
            return redirect('/')
    return render(request, "contact.html")


def search(request):

    return render(request, "search.html")






def reistration(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        password=request.POST['password']
        
        if len(name)<2 or len(email)<3 or len(mobile)<4 or len(password)<4:
            messages.error(request, "Please fill the form correctly")
        # else:
        #     contact=register(name=name, email=email, mobile=mobile, password=password)
        #     contact.save() 
        #     messages.success(request, "Your message has been successfully sent")            
    return render(request,'registrationform.html')


# def login(request):
#     if request.method=="POST":
#         name=request.POST.get('name')
#         password=request.POST.get('password')
        

#         user=authenticate(name=name,password=password)
        
#         if user is not None:
#             login(request, user)
            
#             messages.success(request,'Successfully logged In')
#             return redirect('/login')

#         else:
#             messages.error(request,'User not Signup')
#             return redirect('/login')
#             # return redirect('/')








#     # if request.method=="POST":
#     #     name=request.POST.get('name')
#     #     email=request.POST.get('email')
#     #     password=request.POST.get('password')
#     #     user=register(name=name,email=email,password=password)
        
#     #     if user is not None:
#     #         login(user)
            
#     #         messages.success(request,'Successfully logged In')
#     #         return redirect('/')

#     #     else:
#     #         messages.error(request,'User not Signup')
#     #         return redirect('/') 
            

#     return render(request,'loginform.html')    
     