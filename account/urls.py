from django.urls import path
from .views import GetNewsFeedView, PostNewsFeedView, NewsFeedImageView

urlpatterns = [
    path('newsfeed/get', GetNewsFeedView.as_view()),
    path('newsfeed/post', PostNewsFeedView.as_view()),
     path('api/media/<str:filename>/', NewsFeedImageView.as_view()),

]
