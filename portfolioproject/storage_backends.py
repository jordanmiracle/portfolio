from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class StaticStorage(S3Boto3Storage):
    location = 'static'
    file_overwrite = False
    default_acl = 'public-read'


class MediaStorage(S3Boto3Storage):
    location = settings.DEFAULT_FILE_STORAGE
    default_acl = 'public-read'
    file_overwrite = False
    custom_domain = False
