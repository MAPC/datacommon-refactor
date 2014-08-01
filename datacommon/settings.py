# -*- coding: utf-8 -*-
# Django settings for GeoSolution

import os
import geonode
from urlparse import urlparse

# Main GeoNode directory
GEONODE_ROOT = os.path.dirname(geonode.__file__)
# Find real location if settings file
sfile = __file__
if sfile.endswith('.pyc'):
    sfile = sfile[:-1]
SITE_ROOT = os.path.dirname(os.path.realpath(sfile))


###########################################################
# SITE SPECIFIC SETTINGS
# Overriding generic settings
# Assume development environment. Override in local_settings
###########################################################

SITE_ID = 1
SITENAME = "Datacommon"
# Change to actual URL
SITEURL = 'http://staging.metrobostondatacommon.org/'
SITEURL = 'http://66.181.92.20/'
ROOT_URLCONF = 'geonode.urls'

# Add additional apps here (appended to INSTALLED_APPS)
SITE_APPS = ()

# Make this unique, and don't share it with anybody.
SECRET_KEY = ""
REGISTRATION_OPEN = False
#ACCOUNT_ACTIVATION_DAYS = 7

SOCIAL_BUTTONS = False
LOCKDOWN_GEONODE = False
AUTH_EXEMPT_URLS = ()

ADMINS = (('Admin', 'geo@ags.io'),)
THEME_ACCOUNT_CONTACT_EMAIL = 'geo@ags.io'
ACCOUNT_NOTIFY_ON_PASSWORD_CHANGE = False

# Local time zone for this installation. http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment set to same as your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation.
LANGUAGE_CODE = 'en'

# ASSETS_ROOT is only used on production servers when using collectstatic command
# it is where all the static and media files are served from
ASSETS_ROOT = '/home/datacommon/'
# URL to static web server that serves CSS, uploaded media, javascript, etc.
# for serving from same server or in development, use '/'
ASSETS_URL = '/'

#DEFAULT_WORKSPACE = SITENAME.lower()
#CASCADE_WORKSPACE = SITENAME.lower()
# What is this? (from latest geonode settings)
#OGP_URL = "http://geodata.tufts.edu/solr/select"

# Google API key if using Google maps
#GOOGLE_API_KEY="ABQIAAAAjVRGHcxrLdqVGEtBi5C4vxQAQIK1HEg-uDiqws0W06uxUNVr1RS_xsew-bk3ej5umfL--V2mUdcHEA"

###########################################################
# MODE SPECIFIC SETTINGS
# These settings assume a development environment.
# For production, override these in settings_local
###########################################################

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEBUG_TOOLBAR = DEBUG
DEBUG_STATIC = False

# Default sqlite3 database (flatfile)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join('development.db'),
        'USER': '',     # Not used with sqlite
        'PASSWORD': '', # Not used with sqlite
        'HOST': '',     # Not used with sqlite
        'PORT': ''      # Not used with sqlite
    },
}

###########################################################
# GeoNode specific settings. Rarely should need changing
###########################################################

USE_QUEUE = False

# Do not delete the development database when running tests.
#os.environ['REUSE_DB'] = "1"
# This is needed for integration tests, they require
# geonode to be listening for GeoServer auth requests.
os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS'] = 'localhost:8000'

GEONODE_APPS = (
    # GeoNode internal apps
    'geonode.people',
    'geonode.base',
    'geonode.layers',
    'geonode.maps',
    'geonode.proxy',
    'geonode.security',
    'geonode.social',
    'geonode.catalogue',
    'geonode.documents',
    'geonode.api',
    'geonode.groups',
    'geonode.services',

    # GeoNode Contrib Apps
    'geonode.contrib.dynamic',

    # GeoServer Apps
    # Geoserver needs to come last because
    # it's signals may rely on other apps' signals.
    'geonode.geoserver',
    'geonode.upload',
)

INSTALLED_APPS = (
    # Boostrap admin theme
    # 'django_admin_bootstrapped.bootstrap3',
    # 'django_admin_bootstrapped',

    # Django bundled apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.gis',

    # Utility
    'pagination',
    'taggit',
    'taggit_templatetags',
    'friendlytagloader',
    'geoexplorer',
    'leaflet',
    'django_extensions',
    'autocomplete_light',
    'mptt',
    'modeltranslation',

    # Theme
    'pinax_theme_bootstrap_account',
    'pinax_theme_bootstrap',
    'django_forms_bootstrap',

    # Social
    'account',
    'avatar',
    'dialogos',
    'agon_ratings',
    'notification',
    'announcements',
    'actstream',
    'user_messages',
    'tastypie',
    'polymorphic',
    'guardian',

) + GEONODE_APPS

###########################################################
# MAP DEFAULTS
###########################################################

#DEFAULT_LAYERS_OWNER='admin'
# Where should newly created maps be focused?
DEFAULT_MAP_CENTER = (0, 0)
# How tightly zoomed should newly created maps be?
# 0 = entire world;
# maximum zoom is between 12 and 15 (for Google Maps, coverage varies by area)
DEFAULT_MAP_ZOOM = 10

MAP_BASELAYERS = [{
    "source": {"ptype": "gxp_olsource"},
    "type": "OpenLayers.Layer",
    "args": ["No background"],
    "visibility": False,
    "fixed": True,
    "group":"background"
    }, {
    "source": {"ptype": "gxp_osmsource"},
    "type": "OpenLayers.Layer.OSM",
    "name": "mapnik",
    "visibility": False,
    "fixed": True,
    "group": "background"
    }, {
    "source": {"ptype": "gxp_mapquestsource"},
    "name": "osm",
    "group": "background",
    "visibility": True
    }, {
    "source": {"ptype": "gxp_mapquestsource"},
    "name": "naip",
    "group": "background",
    "visibility": False
    }, {
    "source": {"ptype": "gxp_bingsource"},
    "name": "AerialWithLabels",
    "fixed": True,
    "visibility": False,
    "group": "background"
    }, {
    "source": {"ptype": "gxp_mapboxsource"},
}]

# Documents app
ALLOWED_DOCUMENT_TYPES = [
    'doc', 'docx', 'gif', 'jpg', 'jpeg', 'ods', 'odt', 'pdf', 'png', 'ppt',
    'rar', 'tif', 'tiff', 'txt', 'xls', 'xlsx', 'xml', 'zip',
]
MAX_DOCUMENT_SIZE = 2  # MB

#LAYER_PREVIEW_LIBRARY='geoext'

# Topic Categories list should not be modified (they are ISO). In case you
# absolutely need it set to True this variable
MODIFY_TOPICCATEGORY = False

MISSING_THUMBNAIL = 'geonode/img/missing_thumb.png'
CACHE_TIME = 0

# Uploader Settings
UPLOADER = {
    'BACKEND': 'geonode.rest',
    'OPTIONS': {
        'TIME_ENABLED': False,
        'GEOGIT_ENABLED': False,
    }
}

# Agon Ratings
AGON_RATINGS_CATEGORY_CHOICES = {
    "maps.Map": {
        "map": "How good is this map?"
    },
    "maps.Layer": {
        "layer": "How good is this layer?"
    },
    "documents.Document": {
        "document": "How good is this document?"
    }
}

# Activity Stream
ACTSTREAM_SETTINGS = {
    'MODELS': ('people.Profile', 'layers.layer', 'maps.map', 'dialogos.comment', 'documents.document', 'services.service'),
    'FETCH_RELATIONS': True,
    'USE_PREFETCH': False,
    'USE_JSONFIELD': True,
    'GFK_FETCH_DEPTH': 1,
}

# Setting a custom test runner to avoid running the tests for some problematic 3rd party apps
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--nocapture',
    '--detailed-errors',
    ]

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

LANGUAGES = (
    ('en', 'English'),
    ('es', 'Español'),
    ('it', 'Italiano'),
    ('fr', 'Français'),
    ('de', 'Deutsch'),
    ('el', 'Ελληνικά'),
    ('id', 'Bahasa Indonesia'),
    ('zh-cn', '中文'),
    ('ja', '日本人'),
    ('fa', 'Persian'),
    ('pt', 'Portuguese'),
    ('ru', 'Russian'),
    ('vi', 'Vietnamese'),
    #('fil', 'Filipino'),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_LANGUAGES = ('en', 'es', )

# This isn't required for running the geonode site, but it when running sites that inherit the geonode.settings module.
LOCALE_PATHS = (
    os.path.join(GEONODE_ROOT, "locale"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.tz',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'account.context_processors.account',
    'geonode.context_processors.resource_urls',
    'geonode.geoserver.context_processors.geoserver_urls',
)

# Directories to search for templates
TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates/'),
    os.path.join(GEONODE_ROOT, 'templates/'),
)

# Additional directories which hold static files
STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'static/'),
    os.path.join(GEONODE_ROOT, 'static/')
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Additional directories for fixtures
FIXTURE_DIRS = (os.path.join(SITE_ROOT, 'fixtures'),)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # GeoSolution added
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

AUTH_USER_MODEL = 'people.Profile'
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend','guardian.backends.ObjectPermissionBackend',)

ANONYMOUS_USER_ID = -1
GUARDIAN_GET_INIT_ANONYMOUS_USER = 'geonode.people.models.get_anonymous_user_instance'

LOGIN_URL = '/account/login/'
LOGOUT_URL = '/account/logout/'

DEFAULT_SEARCH_SIZE = 10

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level': 'ERROR',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "ERROR",
        },
        "geonode": {
            "handlers": ["console"],
            "level": "ERROR",
        },

        "gsconfig.catalog": {
            "handlers": ["console"],
            "level": "ERROR",
        },
        "owslib": {
            "handlers": ["console"],
            "level": "ERROR",
        },
        "pycsw": {
            "handlers": ["console"],
            "level": "ERROR",
        },
    },
}

# Used internally later by LEAFLET_CONFIG - seperating facilitates reordering by GeoSites settings
LEAFLET_TILES = {
    # Find tiles at:
    # http://leaflet-extras.github.io/leaflet-providers/preview/
    'Watercolor':       ('Watercolor', 'http://{s}.tile.stamen.com/watercolor/{z}/{x}/{y}.png', 
            'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'),
    'Toner Lite':       ('Toner Lite', 'http://{s}.tile.stamen.com/toner-lite/{z}/{x}/{y}.png', 
            'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'),
    'Terrain':          ('Terrain', 'http://{s}.tile.stamen.com/terrain/{z}/{x}/{y}.png', 
            'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'),
    'OpenStreetMap':    ('OpenStreetMap', 'http://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', 
            '&copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Tiles courtesy of <a href="http://hot.openstreetmap.org/" target="_blank">Humanitarian OpenStreetMap Team</a>'),
    'Landscape':        ('Landscape', 'http://{s}.tile.thunderforest.com/landscape/{z}/{x}/{y}.png', 
            '&copy; <a href="http://www.opencyclemap.org">OpenCycleMap</a>, &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'),

}

LEAFLET_CONFIG = {
    'TILES': [
        LEAFLET_TILES['Watercolor'],
        LEAFLET_TILES['Toner Lite'],
        LEAFLET_TILES['Terrain'],
        LEAFLET_TILES['OpenStreetMap'],
        LEAFLET_TILES['Landscape'],
    ],
    'PLUGINS': {
        'esri-leaflet': {
            'js': 'lib/js/esri-leaflet.js',
            'auto-include': True,
        },
    }
}

# A tuple of hosts the proxy can send requests to.
PROXY_ALLOWED_HOSTS = ('.ags.io',)
ALLOWED_HOSTS = (urlparse(SITEURL).netloc,)

#Enable Licenses User Interface
#Regardless of selection, license field stil exists as a field in the Resourcebase model.
#Detail Display: above, below, never
#Metadata Options: verbose, light, never
LICENSES = {
    'ENABLED': True,
    'DETAIL': 'above',
    'METADATA': 'verbose',
}

# Haystack Search Backend Configuration.  To enable, first install the following:
# - pip install django-haystack
# - pip install pyelasticsearch
HAYSTACK_SEARCH = False
#Avoid permissions prefiltering
SKIP_PERMS_FILTER = False
#Update facet counts from Haystack
HAYSTACK_FACET_COUNTS = False
#HAYSTACK_CONNECTIONS = {
#    'default': {
#        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
#        'URL': 'http://127.0.0.1:9200/',
#        'INDEX_NAME': 'geonode',
#        },
#    }
#HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
#HAYSTACK_SEARCH_RESULTS_PER_PAGE = 20

# Available download formats
DOWNLOAD_FORMATS_METADATA = [
    'Atom', 'DIF', 'Dublin Core', 'ebRIM', 'FGDC', 'TC211',
]
DOWNLOAD_FORMATS_VECTOR = [
    'JPEG', 'PDF', 'PNG', 'Zipped Shapefile', 'GML 2.0', 'GML 3.1.1', 'CSV', 
    'Excel', 'GeoJSON', 'KML', 'View in Google Earth', 'Tiles',
]
DOWNLOAD_FORMATS_RASTER = [
    'JPEG', 'PDF', 'PNG', 'ArcGrid', 'GeoTIFF', 'Gtopo30', 'ImageMosaic', 'KML',
    'View in Google Earth', 'Tiles',
]

TASTYPIE_DEFAULT_FORMATS = ['json']

# gravatar settings
AUTO_GENERATE_AVATAR_SIZES = (20, 32, 80, 100, 140, 200)

# Number of results per page listed in the GeoNode search pages
CLIENT_RESULTS_LIMIT = 100

# Number of items returned by the apis 0 equals no limit
API_LIMIT_PER_PAGE = 0

CACHES = {
    #DUMMY CACHE FOR DEVELOPMENT
    #'default': {
    #    'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    #    },
    #MEMCACHED EXAMPLE
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    #     'LOCATION': '127.0.0.1:11211',
    #     },
    #FILECACHE EXAMPLE
     'default': {
         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
         'LOCATION': '/tmp/django_cache',
         }
}

###########################################################
# Read in local_settings to override Site and Mode settings
###########################################################

APP_SERVER = 'http://localhost:8080/'
# Site local_settings
f = os.path.join(SITE_ROOT, 'local_settings.py')
if os.path.isfile(f):
    execfile(f)
    APP_SERVER = SITEURL

###########################################################
# Locations that might have changed after settings_local
###########################################################

# The proxy to use when making cross origin requests.
PROXY_URL = '/proxy/?url=' if DEBUG else None

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(ASSETS_ROOT, 'media/')
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = os.path.join(ASSETS_URL, 'media/')

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(ASSETS_ROOT, 'static/')

# URL that handles the static files like app media.
STATIC_URL = os.path.join(ASSETS_URL, 'static/')

# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default' : {
        'BACKEND' : 'geonode.geoserver',
        #'LOCATION' : APP_SERVER + 'geoserver/',
        'LOCATION': APP_SERVER + 'geoserver/',
        # PUBLIC_LOCATION needs to be kept like this because in dev mode
        # the proxy won't work and the integration tests will fail
        # the entire block has to be overridden in the local_settings
        #'PUBLIC_LOCATION': '/geoserver/',
        'PUBLIC_LOCATION' : APP_SERVER + 'geoserver/',
        'USER' : 'admin',
        'PASSWORD' : 'geoserver',
        'MAPFISH_PRINT_ENABLED' : True,
        'PRINT_NG_ENABLED' : True,
        'GEONODE_SECURITY_ENABLED' : True,
        'GEOGIT_ENABLED' : False,
        'WMST_ENABLED' : False,
        'BACKEND_WRITE_ENABLED': True,
        'WPS_ENABLED' : True,
        'DATASTORE': 'geodata',
        'TIMEOUT': 10
    }
}

CATALOGUE = {
    'default': {
        # The underlying CSW implementation
        # default is pycsw in local mode (tied directly to GeoNode Django DB)
        'ENGINE': 'geonode.catalogue.backends.pycsw_local',
        # pycsw in non-local mode
        #'ENGINE': 'geonode.catalogue.backends.pycsw_http',
        # GeoNetwork opensource
        #'ENGINE': 'geonode.catalogue.backends.geonetwork',
        # deegree and others
        #'ENGINE': 'geonode.catalogue.backends.generic',

        # The FULLY QUALIFIED base url to the CSW instance for this GeoNode
        'URL': '%scatalogue/csw' % SITEURL,
        #'URL': 'http://localhost:8080/geonetwork/srv/en/csw',
        #'URL': 'http://localhost:8080/deegree-csw-demo-3.0.4/services',

        # login credentials (for GeoNetwork)
        'USER': 'admin',
        'PASSWORD': 'admin',
    }
}

# pycsw settings
PYCSW = {
    # pycsw configuration
    'CONFIGURATION': {
        'metadata:main': {
            'identification_title': 'GeoNode Catalogue',
            'identification_abstract': 'GeoNode is an open source platform that facilitates the creation, sharing, and collaborative use of geospatial data',
            'identification_keywords': 'sdi,catalogue,discovery,metadata,GeoNode',
            'identification_keywords_type': 'theme',
            'identification_fees': 'None',
            'identification_accessconstraints': 'None',
            'provider_name': 'Organization Name',
            'provider_url': SITEURL,
            'contact_name': 'Lastname, Firstname',
            'contact_position': 'Position Title',
            'contact_address': 'Mailing Address',
            'contact_city': 'City',
            'contact_stateorprovince': 'Administrative Area',
            'contact_postalcode': 'Zip or Postal Code',
            'contact_country': 'Country',
            'contact_phone': '+xx-xxx-xxx-xxxx',
            'contact_fax': '+xx-xxx-xxx-xxxx',
            'contact_email': 'Email Address',
            'contact_url': 'Contact URL',
            'contact_hours': 'Hours of Service',
            'contact_instructions': 'During hours of service. Off on weekends.',
            'contact_role': 'pointOfContact',
        },
        'metadata:inspire': {
            'enabled': 'true',
            'languages_supported': 'eng,gre',
            'default_language': 'eng',
            'date': 'YYYY-MM-DD',
            'gemet_keywords': 'Utility and governmental services',
            'conformity_service': 'notEvaluated',
            'contact_name': 'Organization Name',
            'contact_email': 'Email Address',
            'temp_extent': 'YYYY-MM-DD/YYYY-MM-DD',
        }
    }
}

if SITE_APPS:
    INSTALLED_APPS += SITE_APPS

if 'geonode.geoserver' in INSTALLED_APPS:
    LOCAL_GEOSERVER = {
        "source": {
            "ptype": "gxp_wmscsource",
            "url": OGC_SERVER['default']['PUBLIC_LOCATION'] + "wms",
            "restUrl": "/gs/rest"
        }
    }
    baselayers = MAP_BASELAYERS
    MAP_BASELAYERS = [LOCAL_GEOSERVER]
    MAP_BASELAYERS.extend(baselayers)

if LOCKDOWN_GEONODE:
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('geonode.security.middleware.LoginRequiredMiddleware',)

#if DEBUG_TOOLBAR:
if False:
    # Add internal IP Addresses.
    #AGS_INTERNAL_IPS = tuple('10.0.0.{}'.format(x+2) for x in xrange(253))
    #INTERNAL_IPS = ('127.0.0.1') + AGS_INTERNAL_IPS

    DEBUG_TOOLBAR_PATCH_SETTINGS = False
    def always_show_toolbar(request): return True
    def show_if_superuser(request): return True if request.user.is_superuser else False
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar',)
    DEBUG_TOOLBAR_CONFIG = {
        #'INTERCEPT_REDIRECTS': False,
        'SHOW_TOOLBAR_CALLBACK': 'datacommon.settings.show_if_superuser',
    }
