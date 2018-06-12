from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish', 'status')

	list_filter = ('status', 'created', 'publish', 'author')
	search_fields = ('title','body')
	prepopulated_fields = {'slug': ('title',)}
	date_hierarchy = 'publish'
	raw_id_fields = ['author']
	ordering = ['status', 'publish']
admin.site.register(Post, PostAdmin)


# Register comment model admin
from .models import Post, Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
admin.site.register(Comment, CommentAdmin)
