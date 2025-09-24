from django.shortcuts import render
from rest_framwork.viewsets import ModelViewSet
from .models import LongQuestion
from .serializers import LongQuestionSerializer



# Create your views here.
class LongQuestionViewSet(ModelViewSet):
    queryset = LongQuestion.objects.all(many=True)
    serializer_class = LongQuestionSerializer