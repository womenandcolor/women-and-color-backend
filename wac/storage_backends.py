from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = settings.AWS_MEDIA_LOCATION
    file_overwrite = False

class StaticStorage(S3Boto3Storage):
    location = settings.AWS_STATIC_LOCATION