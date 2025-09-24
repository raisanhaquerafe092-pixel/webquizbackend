from django.db import models

# Create your models here.

class LongQuestion(models.Model):
    class_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question