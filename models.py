from django.db import models


# Create your models here.

class file(models.Model):
    csv = models.FileField(blank=False, null=False, upload_to='media/csv')
    uploaded_by = models.CharField(max_length=600, default="admin")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.csv)


class csv_data(models.Model):
    api = models.CharField(max_length=700, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    # data = models.JSONField(null=False, blank=False)

    def __str__(self):
        return str(self.api)


class Email_Schedule(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    send = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.send)


class Slack_Schedule(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    send = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.send)


class CLS_Handler(models.Model):
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(f"{self.url}: {self.created_at}")

    class Meta:
        app_label = "ping_check"
