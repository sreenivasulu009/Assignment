from rest_framework import serializers
from .models import Printers, PrinterIssues, Solutions


class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrinterIssues
        fields = "__all__"


class SolutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solutions
        fields = "__all__"


class PrintersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printers
        fields = "__all__"
