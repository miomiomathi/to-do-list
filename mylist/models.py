from django.db import models
from datetime import date
from django.utils import timezone


# Create your models here.
class ListItem(models.Model):
    created_at = models.DateField(default=date.today)
    item_text = models.CharField(max_length=200)
    done = models.BooleanField(default=False)