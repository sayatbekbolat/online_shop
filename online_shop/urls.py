from django.urls import include, path
from rest_framework import routers
from . import views

routers = routers.DefaultRouter()
routers.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]