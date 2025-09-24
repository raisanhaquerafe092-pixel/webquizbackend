from rest_framework.viewsets import ModelViewSet
from .models import Chapter
from .serializer import ChapterSerializer


class ChapterViewSet(ModelViewSet):
	queryset = Chapter.objects.all()
	serializer_class = ChapterSerializer

	def get_queryset(self):
		qs = super().get_queryset()
		class_name = self.request.query_params.get('class_name')
		subject = self.request.query_params.get('subject')
		if class_name:
			qs = qs.filter(class_name__iexact=class_name)
		if subject:
			qs = qs.filter(subject__iexact=subject)
		return qs


