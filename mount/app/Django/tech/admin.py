from django.contrib import admin
from .models import Article

class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ('title')

# Register your models here.
admin.site.register(Article)