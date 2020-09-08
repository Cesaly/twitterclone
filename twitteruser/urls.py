from django.urls import path
from twitteruser import views


urlpatterns = [
    path('follow/<int:id>/', views.follow_view),
    path('unfollow/<int:id>/', views.unfollow_view),
    path('profile/<int:current_id>/', views.profile_view),
]
