from django.contrib import admin
from .models import *
    
    
class GigManagerInline(admin.TabularInline):
    model = GigManager
    
    
class GigAdmin(admin.ModelAdmin):
    inlines = [
        GigManagerInline
    ]
    
    
admin.site.register(Package)
admin.site.register(Gig, GigAdmin)
admin.site.register(GigManager)
admin.site.register(Seller)
admin.site.register(Order)
