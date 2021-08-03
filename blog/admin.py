from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'content',)
