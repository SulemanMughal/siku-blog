from django.contrib import admin

# Register your models here.

from .models import Category, Post

class PostAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "publish"
    ]

    prepopulated_fields = {
        "slug": (
            "title",
        )
    }

admin.site.register(Category)
admin.site.register(Post, PostAdmin)