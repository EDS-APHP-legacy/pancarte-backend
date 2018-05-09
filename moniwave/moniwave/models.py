import uuid
import datetime

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(default=datetime.date.today)

    class Meta:
        abstract = True
