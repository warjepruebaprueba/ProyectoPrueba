from django.contrib import admin
from .models import Lista

class ListaAdmin(admin.ModelAdmin):
    list_display = ('contenido' ,'pago' ,'pagado',)
    list_filter = ('contenido' ,'pago' ,'pagado',)
    search_fields = ('contenido' ,'pago' ,'pagado',)

admin.site.register(Lista, ListaAdmin)

