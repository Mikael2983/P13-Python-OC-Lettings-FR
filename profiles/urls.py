from django.urls import path

from . import views


# List of URL patterns for the profiles app
urlpatterns = [
    path('', views.index, name='profiles_index'),
    path('<str:username>/', views.profile, name='profile'),
]
