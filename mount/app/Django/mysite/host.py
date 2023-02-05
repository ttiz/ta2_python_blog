from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
                         # host('', settings.ROOT_URLCONF, name=''),
                         host('tech', 'tech.urls', name='tech'),
                         host('social', 'social.urls', name='social'),
                         )
