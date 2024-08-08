from rest_framework import serializers
# from.models import Beach
# from.models import Video
from.models import Girls ,  Photo , Video , User , Creator
from cloudinary.uploader import upload








class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']




class GirlsSerializer(serializers.ModelSerializer):
 class Meta:
   model = Girls
   fields = '__all__'
   

        
        
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
        
        
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'




class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = '__all__'
   

   





