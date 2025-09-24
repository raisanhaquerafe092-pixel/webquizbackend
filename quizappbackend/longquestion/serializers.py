from serializers import ModelSerializer
from .models import LongQuestion

class LongQuestionSerializer(ModelSerializer):
    class Meta:
        model = LongQuestion
        fields = '__all__'