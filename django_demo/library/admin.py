from django.contrib import admin
from .models import Uzrasas, Kategorija



class UzrasasAdmin(admin.ModelAdmin):
    list_display = ('title', 'kategorija_name',)
    list_filter = ('kategorija__first_name',)
    #inlines = [UzrasaiInstanceInline]


class KategorijaAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'display_uzrasai')
    search_fields = ('first_name',)
    


admin.site.register(Uzrasas, UzrasasAdmin)
#admin.site.register(UzrasasInstance, UzrasasInstanceAdmin)
admin.site.register(Kategorija, KategorijaAdmin)
#admin.site.register(Genre)
