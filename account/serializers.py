from rest_framework import serializers
from django.conf import settings
from .models import NewsFeed

class NewsFeedSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = NewsFeed
        fields = ('id','caption', 'image',)

