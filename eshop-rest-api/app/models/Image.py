from django.db.models import Model
from django.db import models
import uuid

from .Product import Product


class Image(Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    
