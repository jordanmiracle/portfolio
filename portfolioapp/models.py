from django.db import models
from django.urls import reverse


# from portfolioproject.storage_backends import MediaStorage, PublicMediaStorage


class Project(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=750, blank=True, null=True)
    url = models.URLField(blank=True)
    code_url = models.URLField(blank=True)
    image = models.ImageField(null=False, blank=False, storage=MediaStorage, upload_to='')
    #image = models.ImageField(null=False, blank=False, upload_to='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', args=[(str(self.id))])
