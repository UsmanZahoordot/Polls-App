from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.show_choices, name='show_choices'),
    path('<int:question_id>/result', views.voted, name='voted')
]
