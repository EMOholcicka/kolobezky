from django.urls import re_path
from django.contrib import admin

from .views import (
    FacebookWebhookView
    )

app_name ='bot_webhooks'
urlpatterns = [
    re_path('messanger/', FacebookWebhookView.as_view(), name='webhook'),
]
