from django.contrib import admin
from .models import *

# Register your models here.

class Tanfelo_TantargyAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request).filter(tantargygondozoi=request.user)    
        return queryset

admin.site.register(Tanfelo_Tantargy, Tanfelo_TantargyAdmin),
# admin.site.register(Tanfelo_Tantargy),
admin.site.register(Tanfelo_Tanar),

class Tanfelo_TanulocsoportAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        tantargyak = Tanfelo_Tantargy.objects.filter(tantargygondozoi=request.user)
        if tantargyak.first() != None:
            queryset = super().get_queryset(request).filter(lehetseges_tantargyai=tantargyak[0])
            for tantargy in tantargyak[1:]:
                queryset.union(super().get_queryset(request).filter(lehetseges_tantargyai=tantargy))
            return queryset
        return None

admin.site.register(Tanfelo_Tanulocsoport, Tanfelo_TanulocsoportAdmin),
admin.site.register(Tanfelo_Kmk),
admin.site.register(Tanfelo_Csoportbontasi_szempont),
admin.site.register(Tanfelo_Csoportbontas),
