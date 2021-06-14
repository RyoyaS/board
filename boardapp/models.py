from django.db import models
from django.db.models.fields import CharField


class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    snsimage = models.ImageField(upload_to="", null=True, blank=True)
    good = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    readtext = models.TextField(null=True, blank=True, default="")

    def __str__(self):
        return self.title
