import os
import dj_database_url

DATABASES = {
}

DB_URL = os.environ.get("DB_URL")

DATABASES['default'] = dj_database_url.config(default=DB_URL)
