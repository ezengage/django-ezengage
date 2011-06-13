from django.conf.urls.defaults import *

urlpatterns = patterns('eze_auth.views',
  url(r'^token_cb/', 'token_login', name='eze_token_login'),
)
