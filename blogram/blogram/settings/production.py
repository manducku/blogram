from .partials import *
import os

DEBUG = False

ALLOWED_HOSTS = [
       "*",
        ]

STATICFILES_STORAGE = 'blogram.storage.S3PipelineCachedStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")

AWS_S3_CUSTOM_DOMAIN = 'd15irv28b5ifxq.cloudfront.net'
AWS_S3_URL_PROTOCOL = 'https'
STATIC_URL = 'https://d15irv28b5ifxq.cloudfront.net/'
