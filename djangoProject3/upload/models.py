from adaptor.model import CsvModel
from adaptor.fields import CharField, IntegerField, DateField
from django.db import models

class  MyCSvModel (CsvModel):
    customer = CharField()
    item = CharField()
    total = IntegerField()
    quantity = IntegerField()
    date = DateField()



"""class UploadCSVModel(models.Model):
    customer = models.CharField(max_length=160)
    item = models.CharField(max_length=160)
    total = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField()"""

class Meta:
    delimiter = ","

