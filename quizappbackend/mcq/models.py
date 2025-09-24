from django.db import models

# Create your models here.


class Mcq(models.Model):
    class_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    question = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.IntegerField()

    def __str__(self):
        return self.question