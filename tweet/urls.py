from django.urls import path
from tweet import views

urlspatterns = [
    path('', views.index, name='homepage'),
    path('tweet/<int:tweet_id>', views.Tweet_detail),
    path('newtweet/', views.NewTweet),
]
