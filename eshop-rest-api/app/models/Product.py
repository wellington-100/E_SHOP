from django.db.models import Model
from django.db import models
import uuid

class Product(Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=512, blank=False, null=False)
    image = models.CharField(max_length=128, blank=False, null=False)
    description = models.CharField(max_length=4096)
    price_standard = models.OneToOneField("Money", on_delete=models.CASCADE, related_name="price_standard_reverse")
    price_discount = models.OneToOneField("Money", on_delete=models.CASCADE, related_name="price_dicount_reverse")
    