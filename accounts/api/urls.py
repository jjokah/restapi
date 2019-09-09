from django.conf.urls import url
from django.contrib import admin

from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token  # accounts app

from .views import AuthAPIView, RegisterAPIView

urlpatterns = [
    url(r'^$', AuthAPIView.as_view()),
    url(r'^register/$', RegisterAPIView.as_view()),
    url(r'^jwt/$', obtain_jwt_token),
    url(r'^jwt/refresh/$', refresh_jwt_token),
]
