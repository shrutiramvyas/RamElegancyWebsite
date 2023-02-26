from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="Ramshop"),
    path('s/',views.s,name="s"),
    path('products/<int:myid>',views.prodview, name="prodView"),
    path('p_stone/', views.p_stone, name="p_Stone"),
    path('contact/', views.contact, name="Contact"),
    path('sp_stone/', views.sp_stone, name="sp_stone"),
    path('jewel/', views.jewel, name="Jewel"),
    path('diamond/', views.diamond, name="Diamond"),
    path('pearl/', views.pearl, name="Pearl"),
    path('cateye/',views.cateye, name="cateye"),
    path('emerald/',views.emerald, name="emerald"),
    path('garnet/', views.garnet, name="Garnet"),
    path('y_sapphire/', views.y_sapphire, name="Yellow Sapphire"),
    path('b_sapphire/',views.b_sapphire, name="Blue Sapphire"),
    path('coral/',views.coral, name="Coral"),
    path('ruby/',views.ruby, name="Ruby"), 
    path('form/',views.newsignup, name="form"), 
    path('checkout/',views.checkout,name="checkout"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

