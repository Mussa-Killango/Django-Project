from django.db import models


class FarmItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2083)
    image_url = models.CharField(max_length=2083)
    pdf_url = models.CharField(max_length=2083)

