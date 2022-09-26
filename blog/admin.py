from django.contrib import admin

from .models import Post, Comment, PostCategory

# Register your models here.
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'writed_at']


admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)