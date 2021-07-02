from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('signup/', views.signup),
    path('', views.home),
    path('logout/', views.logout),
    path('createcontest/', views.create_contest)
]
