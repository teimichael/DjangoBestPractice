from datetime import datetime

from django.db import models


class BaseModel(models.Model):
    """ BaseModel

    Attributes:
        created_at: Created Time
        updated_at: Updated Time
        deleted_at: Deleted Time
    """
    created_at = models.DateTimeField('created time', default=datetime.now)
    updated_at = models.DateTimeField('updated time', auto_now=True)
    deleted_at = models.DateTimeField('deleted time', blank=True, null=True)

    class Meta:
        abstract = True
