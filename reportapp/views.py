from django.db.models import Sum, F, Window
from django.db.models.functions import RowNumber
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import GithubLanguage

class ReportAPIViewORM(APIView):
    def get(self, request):
        lang_stats = (
            GithubLanguage.objects
            .values("year", "name")
            .annotate(total_size=Sum("size"))
            .annotate(
                rownum=Window(
                    expression=RowNumber(),
                    partition_by=[F("year")],
                    order_by=F("total_size").desc()
                )
            )
            .filter(rownum__lte=5)
            .order_by("year", "-total_size")
        )
        return Response(list(lang_stats))
