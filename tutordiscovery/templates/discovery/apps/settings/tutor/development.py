from ..devstack import *

{% include "discovery/apps/settings/partials/common.py" %}

BACKEND_SERVICE_EDX_OAUTH2_KEY = "{{ DISCOVERY_OAUTH2_KEY_DEV }}"
BACKEND_SERVICE_EDX_OAUTH2_SECRET = "{{ DISCOVERY_OAUTH2_SECRET }}"
BACKEND_SERVICE_EDX_OAUTH2_PROVIDER_URL = "http://lms:8000/oauth2"

SOCIAL_AUTH_EDX_OAUTH2_KEY = "{{ DISCOVERY_OAUTH2_KEY_SSO_DEV }}"
SOCIAL_AUTH_EDX_OAUTH2_SECRET = "{{ DISCOVERY_OAUTH2_SECRET_SSO }}"
SOCIAL_AUTH_EDX_OAUTH2_ISSUER = "http://{{ LMS_HOST }}:8000"
SOCIAL_AUTH_EDX_OAUTH2_URL_ROOT = SOCIAL_AUTH_EDX_OAUTH2_ISSUER
SOCIAL_AUTH_EDX_OAUTH2_PUBLIC_URL_ROOT = SOCIAL_AUTH_EDX_OAUTH2_ISSUER
SOCIAL_AUTH_EDX_OAUTH2_LOGOUT_URL = SOCIAL_AUTH_EDX_OAUTH2_ISSUER + "/logout"

# Disable API caching, which makes it a pain to troubleshoot issues
USE_API_CACHING = False

DISCOVERY_BASE_URL = "{{ DISCOVERY_DEV_BASE_URL }}"
MEDIA_URL = "{{ DISCOVERY_DEV_MEDIA_URL }}"

{{ patch("discovery-development-settings") }}
