from django.contrib import admin

from . import models

admin.site.register(models.GeneroMusical)
admin.site.register(models.Musico)
admin.site.register(models.Banda)
admin.site.register(models.Pertenece)
admin.site.register(models.SolicitudUnirseBanda)