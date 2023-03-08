from django.urls import path
from .views import GetNewsFeedView, PostNewsFeedView

urlpatterns = [
    path('newsfeed/get', GetNewsFeedView.as_view()),
    path('newsfeed/post', PostNewsFeedView.as_view()),
]
