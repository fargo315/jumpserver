from django.urls import path

from .. import api

urlpatterns = [
    path('vault/testing/', api.VaultConnectTestingAPI.as_view(), name='vault-connect-testing')
]
