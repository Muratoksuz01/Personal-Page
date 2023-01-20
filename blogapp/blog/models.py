from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
#işin icine biraz database giriyorsa bu model.py gerekli 

class Category(models.Model):
    name=models.CharField(max_length=150)
    slug=models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)#blank ile bos deger yazıp kayıt et dediğinde hata alıyorduk bunu engelledi artık bos kayıt edebilirsin program kendisi sug oluşturacak 
    
    def __str__(self):
        return self.name# catagoriye girdiğinde catagori isimleri direkt görünyüor

    def save(self,*args,**kwargs):#burada otomatik kayıt etmesi için bir fonsiyon yazıd merak edersen https://www.youtube.com/watch?v=pxz4iXz_OlQ&list=PLXuv2PShkuHzrqh-_ZYuDcHZcoZfeAnad&index=23 bakabilirsin 
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)
    


class Blog(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="blogs")#gerekli resimleri database de tutmak için 
    #description=models.CharField(max_length=255)#eski admin panelinde duz sadece string değer girebileceğin bir text acıyor
    description=RichTextField()#admin panelinde sana html yazabileceğin bir sayfa geliyor istersen düz bir şekildedde yazabilrisin ama
    is_active=models.BooleanField(default=False)
    is_home=models.BooleanField(default=False)
    slug=models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)#blank ile bos deger yazıp kayıt et dediğinde hata alıyorduk bunu engelledi artık bos kayıt edebilirsin program kendisi sug oluşturacak 
    categories=models.ManyToManyField(Category,blank=True)
    #category=models.ForeignKey(Category,default=1,on_delete=models.CASCADE)#cascade :kategori ıd silininced tüm kategori bilgileri silinir ;Set_NUL dersen categori silinirse kategori id si nul olsun bunun null=true demen lazım birde 
    #SET_DEFAULD dersen categori dilindiğinde defauld olarak defauld atadıgın değer atanır 
    def save(self,*args,**kwargs):#burada otomatik kayıt etmesi için bir fonsiyon yazıd merak edersen https://www.youtube.com/watch?v=pxz4iXz_OlQ&list=PLXuv2PShkuHzrqh-_ZYuDcHZcoZfeAnad&index=22 bakabilirsin 
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)
    
    
    def __str__(self):# burada anasayfada bu kutuların isimleri var onu direkt göruyorsun 
        return f"{self.title}"
