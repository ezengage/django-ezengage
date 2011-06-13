from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse

EZENGAGE_API_ROOT = getattr(settings, 'EZENGAGE_API_ROOT', 'http://api.ezengage.com/api/v1/')
EZENGAGE_APP_DOMAIN = settings.EZENGAGE_APP_DOMAIN
EZENGAGE_APP_ID = settings.EZENGAGE_APP_ID
EZENGAGE_APP_KEY = settings.EZENGAGE_APP_KEY


current_site = Site.objects.get_current()
#TODO what about https ? 
EZENGAGE_TOKEN_CB = 'http://%s%s' %(current_site.domain, reverse('eze_token_login'))
