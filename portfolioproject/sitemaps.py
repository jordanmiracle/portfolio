from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from portfolioapp.models import Project


class ProjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Project.objects.all()


class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'http'
