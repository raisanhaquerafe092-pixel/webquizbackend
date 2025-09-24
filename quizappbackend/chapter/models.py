from django.db import models

class Chapter(models.Model):
	class_name = models.CharField(max_length=100)
	subject = models.CharField(max_length=100)
	title = models.CharField(max_length=255)
	index = models.PositiveIntegerField(default=1)
	content = models.TextField(blank=True)

	class Meta:
		unique_together = ("class_name", "subject", "index")
		ordering = ["class_name", "subject", "index"]

	def __str__(self):
		return f"{self.class_name} - {self.subject} - {self.index}. {self.title}"
