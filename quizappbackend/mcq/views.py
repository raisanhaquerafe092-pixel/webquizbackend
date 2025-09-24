from rest_framework.viewsets import ModelViewSet
from .models import Mcq
from .serializers import McqSerializer

# Create your views here.

class McqViewSet(ModelViewSet):
    queryset = Mcq.objects.all(many=True)
    serializer_class = McqSerializer