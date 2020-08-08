from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
	path('test/', views.test, name='test'),
	path('index/', views.index, name='index'),
]
