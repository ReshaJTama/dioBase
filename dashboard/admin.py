from django.contrib import admin

from .models import obatBase
from .models import AppModels
# Register your models here.

admin.site.register(obatBase)

admin.site.register(AppModels)