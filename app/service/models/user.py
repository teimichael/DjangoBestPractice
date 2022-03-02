from django.db import models

from core.models import BaseModel


class User(BaseModel):
    name = models.CharField('Name', max_length=50)
    age = models.IntegerField('Age', default=0)
