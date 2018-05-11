from django.db import models

from moniwave.models import BaseModel


class Hospital(BaseModel):
    name = models.CharField(max_length=254)
    alias = models.CharField(max_length=10)


class Service(BaseModel):
    name = models.CharField(max_length=254)
    alias = models.CharField(max_length=10)
    hospital = models.ForeignKey(to=Hospital, on_delete=models.CASCADE)


class Unit(BaseModel):
    name = models.CharField(max_length=254)
    alias = models.CharField(max_length=10)
    service = models.ForeignKey(to=Service, on_delete=models.CASCADE)


class Bed(BaseModel):
    name = models.CharField(max_length=254)
    alias = models.CharField(max_length=10)
    unit = models.ForeignKey(to=Unit, on_delete=models.CASCADE)
