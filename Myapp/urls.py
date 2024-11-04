from .views import RegistrationViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()


router.register(r'api/registration/', RegistrationViewSet, basename='registration')
urlpatterns = [
    path('', include(router.urls)),
    
]

