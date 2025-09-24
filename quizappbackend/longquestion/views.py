from rest_framework.viewsets import ModelViewSet
from .models import LongQuestion
from .serializer import LongQuestionSerializer



# Create your views here.
class LongQuestionViewSet(ModelViewSet):
    queryset = LongQuestion.objects.all()
    serializer_class = LongQuestionSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        class_name = self.request.query_params.get("class_name")
        subject = self.request.query_params.get("subject")
        if class_name:
            queryset = queryset.filter(class_name__iexact=class_name)
        if subject:
            queryset = queryset.filter(subject__iexact=subject)
        return queryset