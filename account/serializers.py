from .models import NewsFeed
from rest_framework import serializers

class NewsFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsFeed
        fields = ('__all__')