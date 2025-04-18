from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'location', 'created_date', 'published_date')
    list_filter = ('published_date', 'author', 'location')
    search_fields = ('title', 'content', 'location')
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
