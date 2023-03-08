from django.urls import path
from .views import NewsFeedView

urlpatterns = [
    path('newsfeed/get', NewsFeedView.as_view({"get": "get request"})),
    path('newsfeed/post', NewsFeedView.as_view({"post": "post request"})),
]
