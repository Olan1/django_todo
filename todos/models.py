from django.db import models


# Create your models here.
class ToDoItem(models.Model):
    item = models.CharField(max_length=255)
    urgent = models.BooleanField(default=False)