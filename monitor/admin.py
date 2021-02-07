from django.contrib import admin
from monitor.models import lkpFrequency, lkpPing, lkpResult, Sites

class FrequencyAdmin(admin.ModelAdmin):
    list_display=['name','code']
    
class PingAdmin(admin.ModelAdmin):
    list_display=['name','code']

class ResultAdmin(admin.ModelAdmin):
    list_display=['name','code']

class SiteAdmin(admin.ModelAdmin):
    list_display=['name','url','lastCheck']

admin.site.register(lkpFrequency,FrequencyAdmin)
admin.site.register(lkpPing,PingAdmin)
admin.site.register(lkpResult,ResultAdmin)
admin.site.register(Sites,SiteAdmin)
