import uuid

from django.db import models

# Create your models here.

class ShoppingItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    is_purchased = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.name}"