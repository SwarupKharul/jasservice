from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Customer,CustomerAdmin)
