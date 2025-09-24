from serializers import ModelSerializer
from .models import ShortQuestion

class ShortQuestionSerializer(ModelSerializer):
    class Meta:
        model: ShortQuestion
        fields = '__all__'