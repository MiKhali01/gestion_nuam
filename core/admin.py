from django.contrib import admin
from .models import Usuario, Empresa, Instrumento, CalificacionTributaria

admin.site.register(Usuario)
admin.site.register(Empresa)
admin.site.register(Instrumento)
admin.site.register(CalificacionTributaria)
