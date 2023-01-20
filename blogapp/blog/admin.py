from django.contrib import admin
from .models import Blog,Category
from django.utils.safestring import mark_safe # library html nin işlenmesini sağlıyor bunu selected_categories te kullandık  sonra html aslında string ti biz bunu html de ul li vrdı bunara cevirdik 
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display=("title","is_home","is_active","slug","selected_categories")#admin sayfasına gelince başlıgı  ve diğerlerini burakadkileri sadece direkt görmeni saglar
    list_editable=("is_home","is_active")#direkt ana sayfadan bunları editlemenı saglar
    search_fields=("title","description")#ana sayfada arama kutusu koyyor sonra burada desritionları aramanı daha kolay bulmanı sağlar ileride  
    readonly_fields=["slug"]#bloga tıkladıgında slug ları değiştiremessin artık  sadece görmen için 
    list_filter=("is_home","is_active","categories")
    
    
    def selected_categories(self, obj):#buradaki obj model.py altındaki category aslında 
        html="<ul>"
        for category in obj.categories.all():
            html+="<li>"+category.name+"</li>"
        html+="</ul>"
        return mark_safe(html)



        
admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)
