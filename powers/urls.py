from django.urls import path
from powers import views

urlpatterns = [
    path('powers/', views.PowerList.as_view()),
    path('powers/<int:pk>/', views.PowerDetail.as_view()),
]
