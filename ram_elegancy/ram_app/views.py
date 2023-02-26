from django.shortcuts import render
from django.http import HttpResponse
from .models import Jewellery, P_diamond_oval, P_diamond_princess, P_stone,P_pearl,P_emerald,P_cateye,P_ruby,P_coral,P_hessonite_garnet,P_blue_sapphire,P_yellow_sapphire,Contact,Sp_stone,P_diamond_shape,P_diamond_pear,P_diamond_round,P_diamond_list
from math import ceil
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index(request):
    service=P_stone.objects.all()
    if request.method=="GET":
        st=request.GET.get('servicename')
        if st!=None:
            service=P_stone.objects.filter(p_name=st)
    params={'service':service}
    return render(request, 'ram_app/index.html',params)


def p_stone(request):
    p_list=P_stone.objects.all()
    n= len(p_list)
    params={ 'p_stone_list':p_list}
    return render(request, 'ram_app/p-stone.html',params)

def sp_stone(request):
    sp_list = Sp_stone.objects.all()
    n = len(sp_list)
    params = {'sp_stone_list': sp_list, 'length': n}
    return render(request, 'ram_app/sp_stone.html', params)

def jewel(request):
    jewel_list = Jewellery.objects.all()
    n = len(jewel_list)
    params = {'jewel_list': jewel_list, 'length': n}
    return render(request,'ram_app/jewel.html',params)

def diamond(request):
    diamondshape_list=P_diamond_shape.objects.all()
    # diamond_list=P_diamond_list.objects.filter(category_id=category_id).all().values()[0]
    category_id=request.GET.get('category')
    if category_id:
        diamond_list=P_diamond_list.objects.filter(category=category_id)
    else:
        diamond_list=P_diamond_list.objects.all()
    params={'diamondshape_list':diamondshape_list,'diamond_list':diamond_list}
    return render(request,'ram_app/diamond.html',params)
# diamondprincess_list=P_diamond_princess.objects.all()
    # diamondoval_list=P_diamond_oval.objects.all()
    # diamondpear_list=P_diamond_pear.objects.all()
    # diamondround_list=P_diamond_round.objects.all()
    # params={'diamondshape_list':diamondshape_list,'diamondprincess_list':diamondprincess_list,'diamondround_list':diamondround_list,'diamondpear_list':diamondpear_list,'diamondoval_list':diamondoval_list}
def pearl(request):
    pearl_list=P_pearl.objects.all()
    n= len(pearl_list)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'pearl_list':pearl_list}
    return render(request,'ram_app/pearl.html',params)

def emerald(request):
    emerald_list=P_emerald.objects.all()
    n= len(emerald_list)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'emerald_list':emerald_list}
    return render(request,'ram_app/emerald.html',params)

def cateye(request):
    cateye_list=P_cateye.objects.all()
    n= len(cateye_list)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'cateye_list':cateye_list}
    return render(request,'ram_app/cateye.html',params)

def coral(request):
    coral_list=P_coral.objects.all()
    n= len(coral_list)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'coral_list':coral_list}
    return render(request,'ram_app/coral.html',params)

def b_sapphire(request):
    b_sapphire_list=P_blue_sapphire.objects.all()
    n= len(b_sapphire_list)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'b_sapphire_list':b_sapphire_list}
    return render(request,'ram_app/b_sapphire.html',params)

def y_sapphire(request):
    y_sapphire_list=P_yellow_sapphire.objects.all()
    n= len(y_sapphire_list)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'y_sapphire_list':y_sapphire_list}
    return render(request,'ram_app/y_sapphire.html',params)

def garnet(request):
    garnet_list=P_hessonite_garnet.objects.all()
    n= len(garnet_list)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'garnet_list':garnet_list}
    return render(request,'ram_app/garnet.html',params)

def ruby(request):
    ruby_list=P_ruby.objects.all()
    n= len(ruby_list)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'ruby_list':ruby_list}
    return render(request,'ram_app/ruby.html',params)

def prodview(request, myid):
   product=P_diamond_list.objects.filter(id=myid).all().values()[0]
   print(dir(product))
   return render(request,'ram_app/prodView.html', {'product':product})

def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name','')
        phone=request.POST.get('phone','')
        email=request.POST.get('email','')
        desc=request.POST.get('desc','')
        print(name, phone, email, desc)
        contact=Contact(name=name,phone=phone,email=email,desc=desc)
        contact.save()
    return render(request,'ram_app/contact.html')

def checkout(request):
    return render(request, 'ram_app/checkout.html')

def newsignup(request):
    form=UserCreationForm
    return render(request,'ram_app/form.html',{"form:":form}) 

def s(request):
    s_st=list(P_stone.objects.all())
    s_list=s_st[0:3]
    params={'s_sto':s_st}
    return render(request,'ram_app/s.html',params)