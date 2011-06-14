django-ezengage
=============================

Installation
-------------------

1. Download latest version from https://github.com/ezengage/django-ezengage/downloads/
2. Unzip the archive
3. run :: 
   
   python setup.py install

We will laster upload the file into PYPI, so your can install with easy_install .

Configuration
-------------------
add `eze_auth` to INSTALLED_APPS

:: 

  INSTALLED_APPS = (
      #.....
      'eze_auth',
      #....
  }


add `eze_auth.auth_backends.EzEngageBackend`  to AUTHENTICATION_BACKENDS

::

  AUTHENTICATION_BACKENDS = ( 
      'django.contrib.auth.backends.ModelBackend',
      'eze_auth.auth_backends.EzEngageBackend',
  )


add `eze_auth_urls` to url conf 

:: 

  urlpatterns += patterns('',
      (r'^eze/', include('eze_auth.urls')),
  )


Sync database
-----------------

::

  ./manage.py syncdb eze_auth

if you are using South, run 

::

  ./manage.py migrate eze_auth


embed login widget in template
--------------------------------

::

   {% load eze_tags %}
   {% eze_login_widget '/after/login/done/' %}


update status 
------------------------------

::

   from eze_auth.helper import get_api_client
   from eze_auth.models import EzeUserProfile

   identity = EzeUserProfile.objects.get(user=request.user)
   message = 'update status to ... '
   eze_api_client = get_api_client()
   eze_api_client.update_status(identity.identity, message)

