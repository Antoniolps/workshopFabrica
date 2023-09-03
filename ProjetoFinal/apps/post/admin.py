from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    fields = ['title', 'content','date_posted', 'author']