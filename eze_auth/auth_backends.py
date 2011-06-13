from eze_auth.models import EzeUserProfile
from django.contrib.auth.models import User
from eze_auth.ezengageapiclient import EzEngageApiClient
from django.conf import settings
import hashlib

class EzEngageBackend:
    """EzEngageBackend for authentication"""

    def __init__(self, app_key = None):
        if app_key is None:
            self.app_key = settings.EZENGAGE_APP_KEY
        else:
            self.app_key = app_key

    def authenticate(self, eze_token, user = None):
        '''authenticates the token by requesting user information from twitter'''
        #we should call the api 
        apiclient = EzEngageApiClient(settings.EZENGAGE_API_ROOT, self.app_key)
        profile = apiclient.get_profile(eze_token)

        try:
            user_profile = EzeUserProfile.objects.get(identity = profile['identity'])
        except EzeUserProfile.DoesNotExist:
            # Create new user
            if not user:
                preferred_username = profile.get('preferred_username', profile['provider_code'] + '_user')
                same_name_count = User.objects.filter(username=preferred_username).count()
                if same_name_count:
                    username = '%s_%s' % (preferred_username, hashlib.md5(profile['identity'].encode('utf-8')).hexdigest()[:8])
                else:
                    username = preferred_username
                username = username[:30]
                user = User(username = username)
                name = preferred_username
                if 'name' in profile:
                    name = profile['name']
                elif 'display_name' in profile:
                    name = profile['display_name']
                namedata = name.split(None, 1)
                if len(namedata) > 1:
                    first_name, last_name = namedata[0], namedata[1]
                else:
                    first_name, last_name =  name, ''
                user.first_name, user.last_name = first_name, last_name
                if 'email' in profile:
                    user.email = profile['email']
                user.save()

            user_profile = EzeUserProfile(user=user, identity = profile['identity'])
            user_profile.save()

        for field in ['provider_code', 'avatar_url', 'preferred_username', 'display_name', 'name']:
            if field in profile:
                setattr(user_profile, field, profile[field])
        user_profile.save()

        return user_profile.user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except:
            return None
