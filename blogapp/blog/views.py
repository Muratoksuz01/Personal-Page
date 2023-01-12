from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog
# Create your views here.

data={
    "blogs":
    [
        {
            "id":1,
            "title":"komple web geliştirme",
            "image":"1.jpg",
            "is_active":True,
            "is_home":True,
            "description":"cok iyi bir kurs"
        },
        {
            "id":2,
            "title":"python",
            "image":"2.jpg",
            "is_active":True,
            "is_home":True,
            "description":"cok iyi bir kurs"
        },
        {
            "id":3,
            "title":"django",
            "image":"3.jpg",
            "is_active":False,
            "is_home":False,
            "description":"cok iyi bir kurs"
        }
    ]
}



def Index(request):
    context={
        "blogs":Blog.objects.filter(is_home=True,is_active=True)
        #"blogs":Blog.objects.all()#
        #"blogs":data["blogs"]
    }
    return render(request,"blog/index.html",context) 

def blog(request):
    context={
        "blogs":Blog.objects.filter(is_active=True )
        #"blogs":data["blogs"]

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

