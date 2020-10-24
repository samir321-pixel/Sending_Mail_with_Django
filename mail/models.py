from django.db import models


# Create your models here.
class Mail(models.Model):
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=150)

    def __str__(self):
        return self.email
