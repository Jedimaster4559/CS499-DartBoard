###################
# backend/models.py
#
# Contains all of the models
# to be included in the database
###################
import uuid
from django.db import models


# This is a basic model class designed to show backend proof of concept
class DartboardHit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)

    def __str__(self):
        return str(self.x) + ', ' + str(self.y)
