from rest_framework.viewsets import ModelViewSet
from .models import LongQuestion
from .serializer import LongQuestionSerializer



# Create your views here.
class LongQuestionViewSet(ModelViewSet):
    queryset = LongQuestion.objects.all()
    serializer_class = LongQuestionSerializer