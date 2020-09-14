from django.urls import path
from tweet import views

urlspatterns = [
    path('', views.Alt_index.as_view(), name='homepage'),
    path('tweet/<int:tweet_id>/', views.TweetDetail.as_view()),
    path('newtweet/', views.NewTweet.as_view()),
]
