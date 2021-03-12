from django.urls import path
from .views import PrinterAPIView, IssuesAPIView, SolutionAPIView

urlpatterns = [
    path("", PrinterAPIView.as_view()),
    path("issueslist/<int:pk>/", IssuesAPIView.as_view()),
    path("printers_list/", PrinterAPIView.as_view()),
    path("solutions/<int:pk>/", SolutionAPIView.as_view()),
]
