###################
# Describes a darts match
###################
import uuid
from django.db import models


class Match(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    best_of_sets_number = models.IntegerField(default=13)

