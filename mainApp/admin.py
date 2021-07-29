from django.contrib import admin
from .models import Package, Gig, GigManager
    
    
class GigManagerInline(admin.TabularInline):
    model = GigManager
    
    
class GigAdmin(admin.ModelAdmin):
    inlines = [
        GigManagerInline
    ]
    
    
admin.site.register(Package)
admin.site.register(Gig, GigAdmin)
