from django.db import models


class ShortUrls(models.Model):
    ShortUrls = models.CharField(max_length=20)
    long_url =models.URLField("URL", unique=True)
