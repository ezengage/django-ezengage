ezengage django app

How to use
-------------------
add eze_autho to INSTALLED_APPS

:: 

  INSTALLED_APPS = (
      #.....
      'eze_auth',
      #....
  }


add eze_auth.auth_backends.EzEngageBackend  to AUTHENTICATION_BACKENDS

::

  AUTHENTICATION_BACKENDS = ( 
      'django.contrib.auth.backends.ModelBackend',
      'eze_auth.auth_backends.EzEngageBackend',
  )


add  eze_auth_urls to url conf 

:: 

  urlpatterns += patterns('',
      (r'^eze/', include('eze_auth.urls')),
  )

