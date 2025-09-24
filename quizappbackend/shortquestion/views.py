from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import ShortQuestion
from .serializer import ShortQuestionSerializer
# Create your views here.

class ShortQuestionViewSet(ModelViewSet):
    queryset = ShortQuestion.objects.all()
    serializer_class = ShortQuestionSerializer