from django.db import models
from portfolioproject.storage_backends import MediaStorage, PublicMediaStorage

class Project(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=750, blank=True, null=True)
    url = models.URLField(blank=True)
    code_url = models.URLField(blank=True)
    image = models.ImageField(null=True, blank=True, storage=MediaStorage)

    def __str__(self):
        return self.title
