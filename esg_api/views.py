from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Corp, ESGScore
from .serializer import CorpSerializer, ESGScoreSerializer


class CorpList(APIView):
    def get(self, request):
        query_set = Corp.objects.select_related('esgscore').all()
        serializer = CorpSerializer(
            query_set, many=True, context={'request': request})  # using context to pass extra stuff
        return Response(serializer.data)

    def post(self, request):
        return Response({'error': 'this method is not allowed yet'},
                        status=status.HTTP_405_METHOD_NOT_ALLOWED)


class EsgScoreDetail(APIView):
    def get(self, request, pk):
        esg = get_object_or_404(ESGScore, pk=pk)
        serializer = ESGScoreSerializer(esg, context={'request': request})  # serializer.data->dict object
        return Response(serializer.data)

    def put(self, request, pk):
        esg = get_object_or_404(ESGScore, pk=pk)
        serializer = ESGScoreSerializer(esg, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delet(self, request, pk):
        esg = get_object_or_404(ESGScore, pk=pk)
        esg.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
