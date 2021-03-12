from django.contrib import admin
from .models import Printers, PrinterIssues, Solutions


admin.site.register(Printers)
admin.site.register(PrinterIssues)
admin.site.register(Solutions)