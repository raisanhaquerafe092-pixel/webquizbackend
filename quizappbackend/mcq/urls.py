from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import McqViewSets


router = DefaultRouter()
router.register(r'question', McqViewSets, basename='mcqviewset')


urlpatterns = [
    path( '',include(router.urls) ),
]
