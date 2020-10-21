from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost

class BlogPostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    exclude = ('slug', )
    list_display = ('id','titulo','date_created')

admin.site.register(BlogPost,BlogPostAdmin)


