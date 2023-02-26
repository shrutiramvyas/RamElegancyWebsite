from django.db import models
from django.forms import IntegerField

# Create your models here.
class P_stone(models.Model):
    p_name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="p_stone_images",default="")
    path=models.CharField(max_length=300)
    
    
    def __str__(self):  
        return self.p_name

class Sp_stone(models.Model):
    sp_name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="sp_stone_images",default="")

    def __str__(self):  
        return self.sp_name

class Jewellery(models.Model):
    j_name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="jewel_images",default="")

    def __str__(self):  
        return self.j_name

class P_diamond_shape(models.Model):
    ds_name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="diamond_images",default="")
    category_id=models.IntegerField(default=0)

    def __str__(self):  
        return self.ds_name

class P_diamond_list(models.Model):
    d_id=models.AutoField
    category_id=models.IntegerField(default=0)
    diamond_name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="diamond_images",default="")
    d_color=models.CharField(max_length=30)
    d_clearity=models.CharField(max_length=20)
    d_shape=models.CharField(max_length=20)
    d_carat=models.CharField(max_length=20)
    # stone_inclusion=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    d_desc=models.CharField(max_length=30)
    pub_date=models.DateField()

    def __str__(self):  
        return self.diamond_name

class P_diamond_round(models.Model):
    d_id=models.AutoField
    diamondround_name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="diamond_images",default="")
    d_color=models.CharField(max_length=30)
    d_clearity=models.CharField(max_length=20)
    d_shape=models.CharField(max_length=20)
    d_carat=models.CharField(max_length=20)
    # stone_inclusion=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    d_desc=models.CharField(max_length=30)
    pub_date=models.DateField()

    def __str__(self):  
        return self.diamondround_name

class P_diamond_pear(models.Model):
    d_id=models.AutoField
    diamondpear_name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="diamond_images",default="")
    d_color=models.CharField(max_length=30)
    d_clearity=models.CharField(max_length=20)
    d_shape=models.CharField(max_length=20)
    d_carat=models.CharField(max_length=20)
    # stone_inclusion=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    d_desc=models.CharField(max_length=30)
    pub_date=models.DateField()

    def __str__(self):  
        return self.diamondpear_name

class P_diamond_oval(models.Model):
    d_id=models.AutoField
    diamondoval_name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="diamond_images",default="")
    d_color=models.CharField(max_length=30)
    d_clearity=models.CharField(max_length=20)
    d_shape=models.CharField(max_length=20)
    d_carat=models.CharField(max_length=20)
    # stone_inclusion=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    d_desc=models.CharField(max_length=30)
    pub_date=models.DateField()

    def __str__(self):  
        return self.diamondoval_name

class P_diamond_princess(models.Model):
    d_id=models.AutoField
    diamondprincess_name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="diamond_images",default="")
    d_color=models.CharField(max_length=30)
    d_clearity=models.CharField(max_length=20)
    d_shape=models.CharField(max_length=20)
    d_carat=models.CharField(max_length=20)
    # stone_inclusion=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    d_desc=models.CharField(max_length=30)
    pub_date=models.DateField()

    def __str__(self):  
        return self.diamondprincess_name


class P_emerald(models.Model):
    em_id=models.AutoField
    emerald_name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="emerald_images",default="")
    d_color=models.CharField(max_length=30)
    d_clearity=models.CharField(max_length=20)
    d_shape=models.CharField(max_length=20)
    d_carat=models.CharField(max_length=20)
    # stone_inclusion=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    d_desc=models.CharField(max_length=30)
    pub_date=models.DateField()

    def __str__(self):  
        return self.emerald_name


class P_yellow_sapphire(models.Model):
    ys_id=models.AutoField
    ys_name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="ys_images",default="")
    d_color=models.CharField(max_length=30)
    d_clearity=models.CharField(max_length=20)
    d_shape=models.CharField(max_length=20)
    d_carat=models.CharField(max_length=20)
    # stone_inclusion=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    d_desc=models.CharField(max_length=30)
    pub_date=models.DateField()

    def __str__(self):  
        return self.ys_name

class P_blue_sapphire(models.Model):
    bs_id=models.AutoField
    bs_name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="bs_images",default="")
    d_color=models.CharField(max_length=30)
    d_clearity=models.CharField(max_length=20)
    d_shape=models.CharField(max_length=20)
    d_carat=models.CharField(max_length=20)
    # stone_inclusion=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    d_desc=models.CharField(max_length=30)
    pub_date=models.DateField()

    def __str__(self):  
        return self.bs_name

class P_ruby(models.Model):
    ruby_id=models.AutoField
    ruby_name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="ruby_images",default="")
    d_color=models.CharField(max_length=30)
    d_clearity=models.CharField(max_length=20)
    d_shape=models.CharField(max_length=20)
    d_carat=models.CharField(max_length=20)
    # stone_inclusion=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    d_desc=models.CharField(max_length=30)
    pub_date=models.DateField()

    def __str__(self):  
        return self.ruby_name

class P_coral(models.Model):
    coral_id=models.AutoField
    coral_name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="coral_images",default="")
    d_color=models.CharField(max_length=30)
    d_clearity=models.CharField(max_length=20)
    d_shape=models.CharField(max_length=20)
    d_carat=models.CharField(max_length=20)
    # stone_inclusion=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    d_desc=models.CharField(max_length=30)
    pub_date=models.DateField()

    def __str__(self):  
        return self.coral_name

class P_hessonite_garnet(models.Model):
    hg_id=models.AutoField
    hg_name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="hg_images",default="")
    d_color=models.CharField(max_length=30)
    d_clearity=models.CharField(max_length=20)
    d_shape=models.CharField(max_length=20)
    d_carat=models.CharField(max_length=20)
    # stone_inclusion=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    d_desc=models.CharField(max_length=30)
    pub_date=models.DateField()

    def __str__(self):  
        return self.hg_name

class P_pearl(models.Model):
    pearl_id=models.AutoField
    pearl_name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="diamond_images",default="")
    d_color=models.CharField(max_length=30)
    d_clearity=models.CharField(max_length=20)
    d_shape=models.CharField(max_length=20)
    d_carat=models.CharField(max_length=20)
    # stone_inclusion=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    d_desc=models.CharField(max_length=30)
    pub_date=models.DateField()

    def __str__(self):  
        return self.pearl_name

class P_cateye(models.Model):
    cte_id=models.AutoField
    ce_name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="cte_images",default="")
    d_color=models.CharField(max_length=30)
    d_clearity=models.CharField(max_length=20)
    d_shape=models.CharField(max_length=20)
    d_carat=models.CharField(max_length=20)
    # stone_inclusion=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    d_desc=models.CharField(max_length=30)
    pub_date=models.DateField()

    def __str__(self):  
        return self.ce_name


#semi-precious stones

#jewellery

class Ring(models.Model):
   ring_id=models.AutoField
   ring_name=models.CharField(max_length=50,default="")
   image=models.ImageField(upload_to="ring_images",default="")
   price=models.IntegerField(default=0)
   pub_date=models.DateField()
   
   def __str__(self):
       return self.ring_name

class Bangels(models.Model):
   bangels_id=models.AutoField
   bangels_name=models.CharField(max_length=50,default="")
   image=models.ImageField(upload_to="bangels_images",default="")
   price=models.IntegerField(default=0)
   pub_date=models.DateField()
   
   def __str__(self):
       return self.bangels_name

class Mangalsutra(models.Model):
   mangal_id=models.AutoField
   mangal_name=models.CharField(max_length=50,default="")
   image=models.ImageField(upload_to="mangalsutra_images",default="")
   price=models.IntegerField(default=0)
   pub_date=models.DateField()
   
   def __str__(self):
       return self.mangal_name

class Earring(models.Model):
   ear_id=models.AutoField
   ear_name=models.CharField(max_length=50,default="")
   image=models.ImageField(upload_to="earrings_images",default="")
   price=models.IntegerField(default=0)
   pub_date=models.DateField()
   
   def __str__(self):
       return self.ear_name

class Necklace(models.Model):
   neck_id=models.AutoField
   neck_name=models.CharField(max_length=50,default="")
   image=models.ImageField(upload_to="necklace_images",default="")
   price=models.IntegerField(default=0)
   pub_date=models.DateField()
   
   def __str__(self):
       return self.neck_name

class Pendent(models.Model):
   pendent_id=models.AutoField
   pendent_name=models.CharField(max_length=50,default="")
   image=models.ImageField(upload_to="pendent_images",default="")
   price=models.IntegerField(default=0)
   pub_date=models.DateField()
   
   def __str__(self):
       return self.pendent_name

class Nosepin(models.Model):
   nose_id=models.AutoField
   nose_name=models.CharField(max_length=50,default="")
   image=models.ImageField(upload_to="nosepin_images",default="")
   price=models.IntegerField(default=0)
   pub_date=models.DateField()
   
   def __str__(self):
       return self.nose_name

class Bracelet(models.Model):
   bracelet_id=models.AutoField
   bracelet_name=models.CharField(max_length=50,default="")
   image=models.ImageField(upload_to="bracelet_images",default="")
   price=models.IntegerField(default=0)
   pub_date=models.DateField()
   
   def __str__(self):
       return self.bracelet_name

class Contact(models.Model):
   msg_id=models.AutoField(primary_key=True)
   name=models.CharField(max_length=70,default="")
   email=models.CharField(max_length=70,default="")
   phone=models.CharField(max_length=50,default="")
   desc=models.CharField(max_length=100,default="")

   def __str__(self):
       return self.name
