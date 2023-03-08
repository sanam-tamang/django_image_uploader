
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

   