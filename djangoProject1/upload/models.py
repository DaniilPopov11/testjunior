from django.db import models

class Upload(models.Model):
    data = models.FileField()
