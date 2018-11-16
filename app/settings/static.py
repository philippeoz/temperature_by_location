from decouple import config
 
from .base import BASE_DIR, DEBUG
 
 
# Urls to serve media and static files
MEDIA_URL = config('MEDIA_URL', default='/media/')
STATIC_URL = config('STATIC_URL', default='/static/')
 
 
# Media and Static files
STATIC_ROOT = BASE_DIR.child('frontend', 'staticfiles')
MEDIA_ROOT = BASE_DIR.child('media')

STATICFILES_DIRS = [
    BASE_DIR.child('frontend', 'static'),
]
 
# Engines to find static files
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Templates Configs
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.child('frontend', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]