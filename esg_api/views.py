from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, DjangoModelPermissions
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Corp, ESGScore, Customer
from .serializers import CorpSerializer, ESGScoreSerializer, CustomerSerializer
from .filters import EsgScoreFilter
from .permissions import ISAdminOrReadOnly, FullDjangoModelPermissions,ViewCustomerHistoryPermission


class CorpViewSet(ModelViewSet):
    queryset = Corp.objects.select_related('esgscore').all()
    serializer_class = CorpSerializer
    filter_backends = [SearchFilter]
    permission_classes = [ISAdminOrReadOnly]
    search_fields = ['title', 'industry_type']

    def get_serializer_context(self):
        return {'request': self.request}


class EsgScoreViewSet(ModelViewSet):
    queryset = ESGScore.objects.annotate(ticker=F('corp__ticker'))
    serializer_class = ESGScoreSerializer
    lookup_field = 'ticker'
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = EsgScoreFilter
    permission_classes = [ISAdminOrReadOnly]
    ordering_fields = ['esg_score', 'rank', 'environment_pillar', 'governance_pillar', 'social_pillar']


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [FullDjangoModelPermissions]

    @action(detail=True, permission_classes=[ViewCustomerHistoryPermission])
    def history(self, request, pk):
        return Response('ok')

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        customer = Customer.objects.get(user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
