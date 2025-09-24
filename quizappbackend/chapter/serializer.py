from rest_framework.serializers import ModelSerializer
from .models import Chapter


class ChapterSerializer(ModelSerializer):
	class Meta:
		model = Chapter
		fields = '__all__'


