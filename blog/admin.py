from django.contrib import admin
from .models import Post, Categories, Tag, Post_comment
from django.contrib import messages 
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','thumbnail_preview', 'status','tags')
    list_display_links = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}
    list_per_page = 1
    list_editable = ['status']

    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True
    
    # Status here
    # def status(self, obj):
    #     return obj.is_active == 1
    
    # status.boolean = True

    def make_active(self, request, queryset): 
        queryset.update(status = 1) 
        messages.success(request, "Selected Record(s) Marked as Published Successfully !!") 
  
    def make_inactive(self, request, queryset): 
        queryset.update(status = 0) 
        messages.success(request, "Selected Record(s) Marked as Darft Successfully !!") 
  
    admin.site.add_action(make_active, "Make Active") 
    admin.site.add_action(make_inactive, "Make Inactive") 

    def has_view_permission(self, request, obj=None):
        return True

    # def _kw(self, obj):
    #     colors = {
    #         1: 'green',
    #         0: 'yellow',
    #     }
    #     return format_html(
    #         '<span style="background-color:{};">{}</span>',
    #         colors[obj.status],
    #         obj.status,
    #     )

# Modified categories
class CategoryAdmin(admin. ModelAdmin):
    list_display = ('name', 'created_on', 'updated_on')
    search_fields = ['name']
    list_per_page = 2

# Modified Tag
class TagAdmin(admin. ModelAdmin):
    list_display = ('name', 'created_on', 'updated_on')
    search_fields = ['name']
    list_per_page = 2

# Modified categories
class Post_commentAdmin(admin. ModelAdmin):
    list_display = ('name', 'created_on', 'updated_on')
    search_fields = ['name']
    list_per_page = 2


admin.site.register(Post, PostAdmin)
admin.site.register(Categories, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post_comment, Post_commentAdmin)