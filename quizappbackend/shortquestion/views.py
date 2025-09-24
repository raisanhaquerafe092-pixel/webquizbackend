from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import ShortQuestion
from .serializers import ShortQuestionSerializer
# Create your views here.

class ShortQuestionViewSet(ModelViewSet):
    queryset = ShortQuestion.objects.all(many=True)
    serializer_class = ShortQuestionSerializer