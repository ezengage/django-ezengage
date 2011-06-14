from eze_auth.ezengageapiclient import EzEngageApiClient

def get_api_client():
    from eze_auth.settings import EZENGAGE_API_ROOT,EZENGAGE_APP_KEY
    return  EzEngageApiClient(EZENGAGE_API_ROOT, EZENGAGE_APP_KEY)
