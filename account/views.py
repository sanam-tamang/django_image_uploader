
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NewsFeedSerializer
from .models import NewsFeed
from rest_framework import status


class PostNewsFeedView(APIView):

    def post(self,request):
        serializer = NewsFeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetNewsFeedView(APIView):
    def get(self,request):
        data = NewsFeed.objects.all()
        serializer = NewsFeedSerializer(data, many = True)
        return Response(serializer.data)




from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.views import APIView
from rest_framework.response import Response

class NewsFeedImageView(APIView):
    def get(self, request, filename):
        try:
            newsfeed = NewsFeed.objects.get(image=filename)
        except NewsFeed.DoesNotExist:
            return HttpResponseNotFound()
        
        image_data = open(newsfeed.image.path, "rb").read()
        return HttpResponse(image_data, content_type="image/jpeg")

   