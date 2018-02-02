from django.db import models

# Create your models here.

class Scrap(models.Model):
    scrap_id = models.AutoField(primary_key=True)
    scrap_url = models.CharField(max_length=300)
    scrap_title = models.CharField(max_length=300)
    scrap_content = models.TextField()