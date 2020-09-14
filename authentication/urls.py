from django.urls import path

from authentication import views

urlpatterns = [
    path('login/', views.loginview.as_view()),
    path('logout/', views.logoutview),
    path('signup/', views.signupview),
]
