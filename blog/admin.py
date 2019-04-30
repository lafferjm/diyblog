from django.contrib import admin
from blog.models import BlogAuthor, BlogPost, BlogComment


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'post_date')
    list_filter = ('author', 'post_date')


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'author', 'post_date', '__str__')
    list_filter = ('blog', 'author', 'post_date')


admin.site.register(BlogAuthor)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
