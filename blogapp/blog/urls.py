from django.urls import path
from . import views
urlpatterns=[ 
    path("",views.Index ,name="HOME"),
    path("blog",views.blog,name="BLOG"),# gecerli linke bunu eklersen eklediğin hali views.blog a foksiyonuna gider
    path("blog/<slug:slug>",views.blog_datails,name="blog_datails")
]
