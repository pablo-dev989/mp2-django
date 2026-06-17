from django.contrib import admin

from phoneapp.models import Manufacturer, Smartphone

# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(Smartphone)
