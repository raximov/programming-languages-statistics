from .views import ReportAPIViewORM
from django.urls import path

urlpatterns = [
    path('report-orm/', ReportAPIViewORM.as_view()),
]