from django.shortcuts import render
from django.http import HttpResponse
from .models import Jewellery, P_stone,P_pearl,P_diamond,P_emerald,P_cateye,P_ruby,P_coral,P_hessonite_garnet,P_blue_sapphire,P_yellow_sapphire,Contact,Sp_stone
from math import ceil
# Create your views here.
def index(request):
    return render(request, 'ram_app/index.html')


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
    diamond_list=P_diamond.objects.all()
    n= len(diamond_list)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'diamond_list':diamond_list}
    return render(request,'ram_app/diamond.html',params)

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
   product=P_diamond.objects.filter(id=myid)
   print(product)
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