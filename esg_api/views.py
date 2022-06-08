from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from .models import Corp, ESGScore
from .serializer import CorpSerializer, ESGScoreSerializer
from .filters import CorpFilter, EsgScoreFilter


class CorpViewSet(ModelViewSet):
    queryset = Corp.objects.select_related('esgscore').all()
    serializer_class = CorpSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CorpFilter

    def get_serializer_context(self):
        return {'request': self.request}


class EsgScoreViewSet(ModelViewSet):
    queryset = ESGScore.objects.annotate(ticker=F('corp__ticker'))
    serializer_class = ESGScoreSerializer
    lookup_field = 'ticker'
    filter_backends = [DjangoFilterBackend]
    filterset_class = EsgScoreFilter
