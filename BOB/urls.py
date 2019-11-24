from django.urls import path
from BOB import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
]
