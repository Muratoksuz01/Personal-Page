from django.contrib import admin
from .models import Blog,Category
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display=("title","is_home","is_active","slug")#admin sayfasına gelince başlıgı  ve diğerlerini burakadkileri sadece direkt görmeni saglar
    list_editable=("is_home","is_active")#direkt ana sayfadan bunları editlemenı saglar
    search_fields=("title","description")#ana sayfada arama kutusu koyyor sonra burada desritionları aramanı daha kolay bulmanı sağlar ileride  
    readonly_fields=["slug"]#bloga tıkladıgında slug ları değiştiremessin artık  sadece görmen için 

admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)
