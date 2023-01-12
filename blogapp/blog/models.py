from django.db import models
from django.utils.text import slugify
# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=200)
    image=models.CharField(max_length=50)
    description=models.TextField(max_length=200)
    is_active=models.BooleanField(default=False)
    is_home=models.BooleanField(default=False)
    slug=models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)#blank ile bos deger yazıp kayıt et dediğinde hata alıyorduk bunu engelledi artık bos kayıt edebilirsin program kendisi sug oluşturacak 
    
    
    def save(self,*args,**kwargs):#burada otomatik kayıt etmesi için bir fonsiyon yazıd merak edersen https://www.youtube.com/watch?v=pxz4iXz_OlQ&list=PLXuv2PShkuHzrqh-_ZYuDcHZcoZfeAnad&index=22 bakabilirsin 
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)
    
    
    def __str__(self):# burada anasayfada bu kutuların isimleri var onu direkt göruyorsun 
        return f"{self.title}"

class Catagory(models.Model):
    name=models.CharField(max_length=150)
    slug=models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)#blank ile bos deger yazıp kayıt et dediğinde hata alıyorduk bunu engelledi artık bos kayıt edebilirsin program kendisi sug oluşturacak 
    
    def __str__(self):
        return self.name# catagoriye girdiğinde catagori isimleri direkt görünyüor

    def save(self,*args,**kwargs):#burada otomatik kayıt etmesi için bir fonsiyon yazıd merak edersen https://www.youtube.com/watch?v=pxz4iXz_OlQ&list=PLXuv2PShkuHzrqh-_ZYuDcHZcoZfeAnad&index=23 bakabilirsin 
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)
    