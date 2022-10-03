from django.contrib import admin
from .models import Uzrasas, Kategorija

'''
class UzrasaiInstanceInline(admin.TabularInline):
    model = UzrasasInstance
    extra = 0
    readonly_fields = ('id',)
    can_delete = False
    '''


class UzrasasAdmin(admin.ModelAdmin):
    list_display = ('title', 'kategorija_name',)
    list_filter = ('kategorija__first_name',)
    #inlines = [UzrasaiInstanceInline]

'''
class UzrasasInstanceAdmin(admin.ModelAdmin):
    list_display = ('uzrasas', 'status', 'due_back',)
    list_filter = ('status', 'due_back',)
    readonly_fields = ('id',)
    search_fields = ('uzrasas__title',)
    list_editable = ('due_back', 'status')

    fieldsets = (
        ('Bendra informacija', {'fields': ('id', 'uzrasas',)}),
        ('Prieinamumas', {'fields': ('status', 'due_back',)}),
    )
'''

class KategorijaAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'display_uzrasai')
    search_fields = ('first_name',)
    


admin.site.register(Uzrasas, UzrasasAdmin)
#admin.site.register(UzrasasInstance, UzrasasInstanceAdmin)
admin.site.register(Kategorija, KategorijaAdmin)
#admin.site.register(Genre)
