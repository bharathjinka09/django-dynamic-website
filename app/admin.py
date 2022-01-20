from django.contrib import admin
from .models import Post, CarouselImages, About, Contact
# Register your models here.

admin.site.register([Post,CarouselImages,About, Contact])
