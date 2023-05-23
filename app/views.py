from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from app.forms import *
from django.contrib.auth import login
from cart.forms import CartAddProductForm
from orders.models import *


# Create your views here.

class homeview(TemplateView):
    template_name="home.html"
class contactview(TemplateView):
    template_name="contact.html"
def insertcontact(request):
    if request.method=='POST':
        form=contactform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/contact/')
    else:
        form=contactform()
    return render(request,"contact.html",{'form':form})


'''


class arrivalsview(ListView):
    template_name="arrivals.html"
    def get_queryset(self):
        return arrivals.objects.all()'''


class reviewsview(TemplateView):
    template_name="reviews.html"

class aboutview(TemplateView):
    template_name="about.html"

def signup(request):
    if request.method=="POST":
        form=signupform(request.POST)
        if form.is_valid():
            User=form.save()
            login(request,User)
            return redirect('/home/')
    else:
        form=signupform()
    return render(request,"registration/signup.html",{'form':form})


'''class englishview(ListView):
    template_name="english.html"
    def get_queryset(self):
        return english.objects.all()
    
class punjabiview(ListView):
    template_name="punjabi.html"
    def get_queryset(self):
        return punjabi.objects.all()

class hindiview(ListView):
    template_name="hindi.html"
    def get_queryset(self):
        return hindi.objects.all()'''
def featuredview(request,type):
    b=featured.objects.filter(booktype=type)
    return render(request,"featured.html",{'b':b,'type':type})

def bookdetail(request,id):
    pro=featured.objects.get(id=id)
    cart_product_form = CartAddProductForm()
    return render(request,"bookdetail.html",{'pro':pro,'cart_product_form':cart_product_form})        

def Myorderview(request):
    c=OrderItem.objects.select_related('order').filter(order__userid=request.user.id)
    return render(request,"Myorder.html",{'c':c})

def insertview(request):
    if request.method=='POST':
        form=reviewform(request.POST)
        next=request.POST.get('next')
        if form.is_valid():
            form.save()
            return redirect(next)
    else:
        form=reviewform()
    return render(request,"bookdetails.html",{'form':form})

class faqview(ListView):
    template_name="faq.html"
    def get_queryset(self):
        return faq.objects.all()
    
def blogview(request):
    blg=blog.objects.all()
    return render(request,"blog.html",{'blg':blg})

def blogdetailview(request,id):
    pro=blog.objects.get(id=id)
    return render(request,"blogdetail.html",{'pro':pro})
    
class paymentview(TemplateView):
    template_name="payment.html"

class privacyview(TemplateView):
    template_name="privacy.html"

class termsview(TemplateView):
    template_name="terms.html"

class copyrightview(TemplateView):
    template_name="copyright.html"



