from rest_framework.serializers import ModelSerializer

from .models import Mcq

class McqQuestionSerializer(ModelSerializer):
    class Meta:
        model = Mcq
        fields = '__all__'