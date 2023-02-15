from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog,Category
# Create your views here.


def Index(request):
    context={
        "blogs":Blog.objects.filter(is_home=True,is_active=True),
        "categories":Category.objects.all(),#bu parametreyi gönderemiyoruz aynısıs blog ta da var ama burada calışmıyor anlamdaım  
    }
    return render(request,"blog/index.html",context) 
    
def blogs_by_category(request,slug):
    context={
        "blogs":Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        #"blogs":Blog.objects.filter(is_active=True ,category__slug=slug),#models.py dosyasındaki blog clasına gidiyorsun blog clasında cetagory clasına giden bir yer yer onu belirmek için yani blog clasından categorri clasından bir sey istefiğin için 2'__' alt cizgi kullanıyorsun bunu belirmen gerekiyor unutma 
        "categories":Category.objects.all(),
        "selected_category":slug
    }
    return render(request,"blog/blogs.html",context)

def blog(request):
    context={
        "blogs":Blog.objects.filter(is_active=True ),
        "categories":Category.objects.all(),
    }
    return render(request,"blog/blogs.html",context)

def blog_datails(request,slug):
    #blogs=data["blogs"]
    
    # for blog in blogs:
    #     if blog["id"]==id:
    #         selectedblog=blog
    # return render(request,"blog/blogs-datails.html",{"blogs":selectedblog })

    
    blog=Blog.objects.get(slug=slug)
    return render(request,"blog/blogs-datails.html",{"blog":blog})

