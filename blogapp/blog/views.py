from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog,Category
# Create your views here.


def Index(request):
    context={
        "blogs":Blog.objects.filter(is_home=True,is_active=True),
        "catagories":Category.objects.all(),
    }
    return render(request,"blog/index.html",context) 
def blogs_by_category(request,slug):
    pass

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
    return render(request,"blog/blogs-datails.html",{"blogs":blog})

