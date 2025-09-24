from rest_framework.viewsets import ModelViewSet
from .models import Mcq
from .serializer import McqQuestionSerializer

# Create your views here.

class McqViewSet(ModelViewSet):
    queryset = Mcq.objects.all()
    serializer_class = McqQuestionSerializer