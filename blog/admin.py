from django.contrib import admin

from blog.models import AuthorProfile, Comment, Post, Tag


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('slug', 'published_at')


admin.site.register(AuthorProfile)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
