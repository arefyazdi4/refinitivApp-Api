from django.db.models import F
from rest_framework.viewsets import ModelViewSet
from .models import Corp, ESGScore
from .serializer import CorpSerializer, ESGScoreSerializer


class CorpViewSet(ModelViewSet):
    queryset = Corp.objects.select_related('esgscore').all()
    serializer_class = CorpSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class EsgScoreViewSet(ModelViewSet):
    queryset = ESGScore.objects.annotate(ticker=F('corp__ticker'))
    serializer_class = ESGScoreSerializer
    lookup_field = 'ticker'
