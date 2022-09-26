from django.contrib import admin

from .models import OwnerInfo, SocialLink

class OwnerInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'specialize', 'created_at']


class SocalLinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']


admin.site.register(OwnerInfo, OwnerInfoAdmin)
admin.site.register(SocialLink, SocalLinkAdmin)