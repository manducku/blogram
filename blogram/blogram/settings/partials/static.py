import os
from .application import PROJECT_ROOT_DIR, BASE_DIR

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT_DIR, "dist", "media")
STATIC_ROOT = os.path.join(PROJECT_ROOT_DIR, "dist", "static")

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
            'django.contrib.staticfiles.finders.FileSystemFinder',
            'django.contrib.staticfiles.finders.AppDirectoriesFinder',
            'pipeline.finders.PipelineFinder',
                    )

PIPELINE = {
    'PIPELINE_ENABLED': True,
    'JAVASCRIPT': {
    },

    'STYLESHEETS': {
        'application': {
            'source_filenames': (
              'css/*.css',
            ),
            'output_filename': 'css/blogram.css',
        },
    },
  }
