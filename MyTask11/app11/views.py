from django.shortcuts import render, get_object_or_404, Http404
from django.http import HttpResponse, JsonResponse
from .models import Printers, PrinterIssues, Solutions
from .serializers import PrintersSerializer, IssuesSerializer, SolutionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer


class PrinterAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'printers_list.html'

    def get(self, request):
        printer = Printers.objects.all()
        serializer = PrintersSerializer(printer, many=True)
        return Response({'printers': serializer.data})

    def post(self, request):
        serializer = PrintersSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IssuesAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'issues.html'

    def get_object(self, pk):
        printer = Printers.objects.all()
        try:
            return Printers.objects.get(pk=pk)
        except printer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        printer = self.get_object(pk)
        serializer = IssuesSerializer(printer.printerissues.all(), many=True)
        return Response({"issues": serializer.data})


class SolutionAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'solutions.html'

    def get_object(self, issue_id):
        try:
            return PrinterIssues.objects.get(pk=issue_id)
        except printer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        printerissues = self.get_object(pk)
        serializer = SolutionSerializer(printerissues.solution.all(), many=True)
        return Response({"issues": serializer.data})


