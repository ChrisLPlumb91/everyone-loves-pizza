from django.contrib import admin
from .models import CustomerMessage


class CustomerMessageAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'reason',
        'user_msg',
        'created_on',
    )

    ordering = ['-created_on', 'customer']


admin.site.register(CustomerMessage, CustomerMessageAdmin)