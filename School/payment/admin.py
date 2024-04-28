from django.contrib import admin

from payment.models import InvoiceType, Invoice, InvoiceItem

# Register your models here.


admin.site.register(Invoice)
admin.site.register(InvoiceItem)
admin.site.register(InvoiceType)
