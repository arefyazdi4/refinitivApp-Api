from django.db.models import F
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Corp, ESGScore
from .serializer import CorpSerializer, ESGScoreSerializer


class CorpList(ListCreateAPIView):
    queryset = Corp.objects.select_related('esgscore').all()
    serializer_class = CorpSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class EsgScoreDetail(RetrieveUpdateDestroyAPIView):
    queryset = ESGScore.objects.annotate(ticker=F('corp__ticker'))
    serializer_class = ESGScoreSerializer
    lookup_field = 'ticker'
