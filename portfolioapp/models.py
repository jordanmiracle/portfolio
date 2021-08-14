from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=240)
    url = models.URLField(blank=True)
    code_url = models.URLField(blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.title
