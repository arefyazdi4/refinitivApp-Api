from django_filters.rest_framework import FilterSet
from .models import Corp, ESGScore


class CorpFilter(FilterSet):
    class Meta:
        model = Corp
        fields = {
            'title': ['exact', 'contains'],
            'industry_type': ['contains'],
        }


class EsgScoreFilter(FilterSet):
    class Meta:
        model = ESGScore
        fields = {
            'esg_score': ['exact', 'gt', 'lt'],
            'rank': ['exact', 'gt', 'lt'],
            'corp__ticker': ['exact'],
        }
