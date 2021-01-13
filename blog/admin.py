from django.contrib import admin
from .models import Post, Categories, Tag, Post_comment
# from sorl.thumbnail.admin import AdminImageMixin
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','thumbnail_preview', 'status')
    prepopulated_fields = {"slug": ("title",)}
    list_per_page = 1
    
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True
    
    

admin.site.register(Post, PostAdmin)
admin.site.register(Categories)
admin.site.register(Tag)
admin.site.register(Post_comment)