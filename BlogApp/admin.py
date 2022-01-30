from django.contrib import admin
from .models import Category,Post
# Register your models here.
class AdminCategory(admin.ModelAdmin):
    list_display = ['cat_id','imgtagcat','author','title','description','url']
    search_fields = ('title',)
    list_filter = ('title',)
    list_per_page = 5
class AdminPost(admin.ModelAdmin):
    list_display = ['post_id','imgtagpost','author','title','content','url','cat']
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 5
admin.site.register(Category,AdminCategory)
admin.site.register(Post,AdminPost)
