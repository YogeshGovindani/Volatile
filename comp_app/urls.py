from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('signup/', views.signup),
    path('', views.home),
    path('logout/', views.logout),
    path('createcontest/', views.create_contest),
    path('contest/<str:contest_id>', views.contest),
    path('question/<str:question_id>', views.question),
    path('solutions/<str:t>/<str:id>', views.solutions),
    path('solution/<str:solution_id>', views.solution)
]
