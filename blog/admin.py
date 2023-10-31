from django.contrib import admin
from .models import *

# Register your models here.
class Commentiteminline(admin.TabularInline):
    model = Comment
    raw_id_fields=('post',)

class CategoryModel(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title','slug')
    list_filter = ('title',)
    prepopulated_fields = {'slug':('title',)}
admin.site.register(Category,CategoryModel)

class PostModel(admin.ModelAdmin):
    search_fields = ('title','slug','publish_date','intro')
    list_display = ('title','category','publish_date','status','image',)
    list_filter = ('category','status','publish_date',)
    exclude = ('views',)
    prepopulated_fields = {'slug':('title',)}

    inlines = [Commentiteminline]
    
admin.site.register(Post,PostModel)

class CommentModel(admin.ModelAdmin):
    list_display = ('name','post','comment_date',)
    readonly_fields = ('post','name','email','comment','comment_date')
    list_filter = ('post','comment_date',)

admin.site.register(Comment,CommentModel)
