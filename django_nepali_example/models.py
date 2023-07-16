"""Contains models using django-nepali models field"""
from django.db import models
from django_nepali.models import NepaliDateField

class NepaliDateFieldTestModel(models.Model):
    """Test model for NepaliDateField"""
    nepali_date = NepaliDateField()
