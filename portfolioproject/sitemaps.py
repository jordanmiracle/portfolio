from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from portfolioapp.models import Project


class ProjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Project.objects.all()

    def location(self, items):
        return items.url


class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'http'
