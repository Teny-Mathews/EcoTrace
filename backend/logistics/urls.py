from django.urls import path
from .views import AnalyzeWasteView

urlpatterns = [
    path('analyze/', AnalyzeWasteView.as_view(), name='analyze-waste'),
]