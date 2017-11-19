from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    readonly_fields=('timestamp',)
    list_display = ('email', 'full_name', 'company_name' , 'timestamp', 'phone_number',)
    list_filter = ('timestamp',)

# Register your models here.
admin.site.register(Client, ClientAdmin)
