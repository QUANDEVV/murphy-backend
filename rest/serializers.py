from rest_framework import serializers
# from.models import Beach
# from.models import Video
from.models import Auction ,Adverts
from cloudinary.uploader import upload




class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ['id', 'name', 'description', 'category', 'price', 'condition', 'image']



class AdvertsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adverts
        fields = ['id', 'image', 'name', 'description', 'price']
   





