from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from articles.models import  Articles, Authors, Usuario

admin.site.register(Usuario, UserAdmin)

class Article(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'summary', 'firstParagraph', 'author', 'body')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_per_page = 20

admin.site.register(Articles, Article)

class Author(admin.ModelAdmin):
    list_display = ('id', 'name', 'picture')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Authors, Author)
