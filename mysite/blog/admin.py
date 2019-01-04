from django.contrib import admin

# Register your models here.
# 该文件用于将模型注册到 administration 网站。

# 让我们将 blog 模型添加到 admin网站。向 blog 应用的 admin.py 文件写入以下代码：

from .models import Post,Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)
