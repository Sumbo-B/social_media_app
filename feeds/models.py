from django.db import models

# Create your models here.

class Feeds(models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='image/', blank=True, null=True)



class Meta:
        ordering = ("-created_at",)