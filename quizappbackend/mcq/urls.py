from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import McqViewSet


router = DefaultRouter()
router.register(r'question', McqViewSet, basename='mcqviewset')


urlpatterns = [
    path( '',include(router.urls) ),
]
