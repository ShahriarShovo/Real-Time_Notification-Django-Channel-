from django.db import models

# Create your models here.
class Notification(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

