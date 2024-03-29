from django.db.models import Model
from django.db import models
import uuid
from .Client import Client




class Order(Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)


  