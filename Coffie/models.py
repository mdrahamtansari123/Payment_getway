from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Coffee(models.Model):
  name=models.CharField(max_length=70)
  amount=models.CharField(max_length=70)
  payment_id=models.CharField(max_length=70)
  paid=models.BooleanField(default=False)

  def __str__(self):
    return str(self.id)

