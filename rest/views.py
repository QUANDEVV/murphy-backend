from django.http import JsonResponse
# from.models import Beach
# from.serializers import BeachSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from .models import Video
# from .serializers import VideoSerializer
from rest_framework import generics
from .models import Girls
from .serializers import GirlsSerializer
from  django.contrib.auth import logout
from  django.shortcuts import render , redirect
from .models import Auction , Adverts
from .serializers import AuctionSerializer ,AdvertsSerializer
from django.shortcuts import get_object_or_404
import json
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, "home.html")


def logout_view(request):
    logout(request)
    return redirect("/")




@api_view(['GET', 'POST'])
def auction_list(request):
    if request.method == 'GET':
        auctions = Auction.objects.all()
        serializer = AuctionSerializer(auctions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AuctionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def auction_detail(request, pk):
    try:
        auction = Auction.objects.get(pk=pk)
    except Auction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AuctionSerializer(auction)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AuctionSerializer(auction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        auction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    




    # ///// 

@api_view(['GET', 'POST'])
def adverts_list(request):
    if request.method == 'GET':
        adverts = Adverts.objects.all()
        serializer = AdvertsSerializer(adverts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AdvertsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def adverts_detail(request, pk):
    try:
        advert = Adverts.objects.get(pk=pk)
    except Adverts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdvertsSerializer(advert)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AdvertsSerializer(advert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        advert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    

