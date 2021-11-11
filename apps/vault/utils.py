# -*- coding: utf-8 -*-
#
from django.conf import settings

from .backends.vault_client import VaultClient
from .backends.kv import KVEngineVault
from common.utils import get_logger

logger = get_logger(__name__)


def is_model_setting_vault_field_and_active(model):
    if not hasattr(model, 'VAULT_FIELD') or not hasattr(model, 'VAULT_FIELD'):
        return False
    elif hasattr(model, 'vault'):
        return getattr(getattr(getattr(model, 'vault'), 'client'), 'is_active')
    else:
        return True


def instance_read_and_replace_data(instance):
    secret_data = instance.vault.read_secret(instance.pk)
    for k, v in secret_data.items():
        setattr(instance, k, v)


def init_vault_path():
    from assets.models import SystemUser

    vault_models = [SystemUser, ]

    client = VaultClient(settings.VAULT_URL)
    client.check_base_token_authentication(settings.VAULT_TOKEN)

    for model in vault_models:
        if not is_model_setting_vault_field_and_active(model):
            logger.error('{} not specified VAULT_FIELD'.format(model))
        else:
            model_name = model._meta.model_name
            model.vault = KVEngineVault(client, model_name)
