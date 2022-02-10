from django.contrib.sitemaps import Sitemap
from portfolioapp.models import Project
from django.urls import reverse


class ProjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'


class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'http'







