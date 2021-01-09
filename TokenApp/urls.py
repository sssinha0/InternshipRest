from django.contrib import admin
from django.urls import path,include
from . import views
from .auth import CustomAuthToken
urlpatterns = [
   path('studnetapi',views.Studentview),
   path('auth/', include('rest_framework.urls', namespace='rest_framework')),
   path('gettoken/', CustomAuthToken.as_view())
]