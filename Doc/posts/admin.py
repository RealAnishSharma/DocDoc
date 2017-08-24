from django.contrib import admin

# Register your models here.
from posts.models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display=["name","updated","timestamp"]
    list_display_links=["updated"]
    list_editable=["name"]
    list_filter=["updated","timestamp"]
   
    search_fields=["name","remarks","Hospital"]
    class Meta:
        model=Post




admin.site.register(Post,PostModelAdmin)
