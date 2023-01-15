from django.urls import path
from . import views
urlpatterns=[ 
    path("",views.Index ,name="HOME"),
    path("blog",views.blog,name="BLOG"),# gecerli linke bunu eklersen eklediğin hali views.blog a foksiyonuna gider
    path("category/<slug:slug>",views.blogs_by_category,name="blogs_by_category"),
    path("blog/<slug:slug>",views.blog_datails,name="blog_datails")#bundan sonra burada int gibi bir değer değilde string gelecek bu daha okunaklı bir hal alacak 
]
