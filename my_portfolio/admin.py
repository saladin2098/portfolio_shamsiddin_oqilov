from django.contrib import admin

from .models import Study, Experiance, Portfolio, PortfolioCategory
# Register your models here.
class StudyAdmin(admin.ModelAdmin):
    list_display = ['id', 'where', 'specialize', 'degree',\
         'from_date', 'to_date', 'created_at']


class ExperianceAdmin(admin.ModelAdmin):
    list_display = ['id', 'company', 'specialize', 'technalogies',\
         'from_date', 'to_date', 'created_at']

    
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'title', 'link', 'created_at']



admin.site.register(Study, StudyAdmin)
admin.site.register(Experiance, ExperianceAdmin)
admin.site.register(PortfolioCategory, PortfolioCategoryAdmin)
admin.site.register(Portfolio, PortfolioAdmin)