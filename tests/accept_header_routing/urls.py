from django.conf.urls.defaults import *

from api import api_router, custom_api_router

urlpatterns = patterns('',
    (r'^api/(?P<rest>.*)', api_router.as_view()),
    (r'^api_custom_router/(?P<rest>.*)', custom_api_router.as_view()),
)
