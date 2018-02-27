from django.contrib import admin
from blog.models import post


# Register your models here.

class postModelAdmin(admin.ModelAdmin):
    # for displaying more thing in admin page
    list_display = ['title', 'timestamp', 'updated']
    # for displaying link with another attribute
    list_display_links = ['timestamp']
    # for displaying attribute with editable features
    list_editable = ['title']
    # for list filter
    list_filter = ['updated', 'timestamp']
    # setting search field
    search_fields = ['title', 'post_content']

    class Meta:
        model = post


admin.site.register(post, postModelAdmin)
