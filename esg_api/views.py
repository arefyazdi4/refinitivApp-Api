from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Corp, ESGScore
from .serializer import CorpSerializer, ESGScoreSerializer


@api_view(['GET', 'POST'])
def corp_list(request):
    if request.method == 'GET':
        query_set = Corp.objects.select_related('esgscore').all()
        serializer = CorpSerializer(
            query_set, many=True, context={'request': request})  # using context to pass extra stuff
        return Response(serializer.data)
    elif request.method == 'POST':
        return Response({'error': 'this method is not allowed yet'},
                        status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def esg_score(request, pk):
    esg = get_object_or_404(ESGScore, pk=pk)
    if request.method == 'GET':
        serializer = ESGScoreSerializer(esg, context={'request': request})  # serializer.data->dict object
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ESGScoreSerializer(esg, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        esg.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
