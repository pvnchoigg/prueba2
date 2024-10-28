from django.contrib import admin
from app.models import tatuadores

class tatuadorAdmin(admin.ModelAdmin):
    display=['nombre','experiencia','estilo','email','telefono']

# Register your models here.

admin.site.register(tatuadores)