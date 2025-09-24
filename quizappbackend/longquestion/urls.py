from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import LongQuestionViewSet


router = DefaultRouter()
router.register(r'question', LongQuestionViewSet, basename='longquestionviewset')


urlpatterns = [
    path( '',include(router.urls) ),
]
