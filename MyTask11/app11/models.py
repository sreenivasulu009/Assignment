from django.db import models
import uuid


class Printers(models.Model):
    printer_name = models.CharField(max_length=100)
    printer_serial = models.UUIDField(default=uuid.uuid4, editable=False)
    printer_model = models.CharField(max_length=100)
    printer_make = models.DateTimeField(auto_now_add=True)


class PrinterIssues(models.Model):
    printer = models.ForeignKey(Printers, on_delete=models.CASCADE, related_name='printerissues')
    issue_no = models.IntegerField()
    issue_name = models.CharField(max_length=100)


class Solutions(models.Model):
    issue = models.ForeignKey(PrinterIssues, on_delete=models.CASCADE, related_name='solution')
    solution = models.CharField(max_length=225)
