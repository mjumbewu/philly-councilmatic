import os

# Make filepaths relative to settings.
def rel_path(*subs):
    """Make filepaths relative to this settings file"""
    root_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(root_path, *subs)

DEBUG = (os.environ.get('DEBUG', 'False').lower() == 'true')
COMPRESS_ENABLED = not DEBUG
TEMPLATE_DEBUG = DEBUG
DO_DEBUG_TOOLBAR = DEBUG

ADMINS = [
    (admin.split('@')[0], admin)
    for admin in os.environ.get('ADMINS', '').split(',')
]

import dj_database_url
DATABASES = {'default': dj_database_url.config()}
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

###############################################################################
#
# 3rd-party service configuration and keys
#

TWITTER_CONSUMER_KEY         = ''
TWITTER_CONSUMER_SECRET      = ''
FACEBOOK_APP_ID              = ''
FACEBOOK_API_SECRET          = ''
LINKEDIN_CONSUMER_KEY        = ''
LINKEDIN_CONSUMER_SECRET     = ''
GOOGLE_CONSUMER_KEY          = ''
GOOGLE_CONSUMER_SECRET       = ''

RECAPTCHA_PUBLIC_KEY  = ''
RECAPTCHA_PRIVATE_KEY = ''

GOOGLE_ANALYTICS_ACCOUNT = ''
FOOTER_CONTENT = "An app by <a href='http://codeforamerica.org'>Code for America</a>."

###############################################################################
#
# Source Data
#

LEGISLATION = {
    'SYSTEM': 'Granicus Legistar',
    'ROOT': 'http://phila.legistar.com/',
    'ADDRESS_BOUNDS': [39.874439,-75.29892, 40.141615,-74.940491], # lat, lng, lat, lng
    'ADDRESS_SUFFIX': ', Philadelphia, PA',

    'SCRAPER': ('phillyleg.management.scraper_wrappers.sources.'
                'hosted_legistar_scraper.HostedLegistarSiteWrapper'),
    'SCRAPER_OPTIONS': {
        'hostname': 'phila.legistar.com',
        'fulltext': True,
        'sponsor_links': False,

        # Label overrides
        # --------------- 
        'id_label': 'File #',
        'controlling_body_label': 'In control',
        'intro_date_label': 'File Created',
        'topics_label': 'Indexes',
    },
}

###############################################################################
#
# Caching
#
# Using some cache backend is definitely recommended. If you want to use
# memcache, uncomment the lines below and fill in your server information. See
# https://docs.djangoproject.com/en/dev/topics/cache/#setting-up-the-cache for
# other options.
#

#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#        'LOCATION': '127.0.0.1:11211',
#    }
#}

###############################################################################
#
# Topic classifier
#
# Use this to set custom rules for classifying your legislation

TOPIC_CLASSIFIER = lambda title: []

###############################################################################
#
# Site search configuration
#

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': os.environ.get('SEARCH_URL'),
        'INDEX_NAME': 'councilmatic',
    }
}

################################################################################
#
# Testing and administration
#
# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },

    'filters': {
        'only_when_debug_is_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },

    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter':'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
            'filters': ['only_when_debug_is_false'],
        }
    },

    'loggers': {
        'django': {
            'handlers':['null'],
            'propagate': True,
            'level':'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'WARNING',
            'propagate': False,
        },
        'councilmatic': {
            'handlers': ['console', 'mail_admins'],
            'level': 'DEBUG',
        },
        'phillyleg.management': {
            'handlers': ['console', 'mail_admins'],
            'level': 'DEBUG',
        },
    }
}
