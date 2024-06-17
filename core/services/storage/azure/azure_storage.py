from io import BytesIO
from pathlib import Path

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import BlobClient

from django.conf import settings

import uuid

from core.services.storage.allowed_files import ALLOWED_FILES


class Storage():

    @staticmethod
    def create_blob_client(file_name):
        default_credential = DefaultAzureCredential()

        secret_client = SecretClient(
            vault_url=settings.AZURE_VAULT_ACCOUNT,
            credential=default_credential
        )

        storage_credentials = secret_client.get_secret(
            name=settings.AZURE_STORAGE_KEY_NAME
        )

        return BlobClient(
            account_url=settings.AZURE_STORAGE_ACCOUNT,
            container_name=settings.AZURE_APP_BLOB_NAME,
            blob_name=file_name,
            credential=storage_credentials.value
        )

    @staticmethod
    def check_file_ext(path):
        ext = Path(path).suffix
        return ext in ALLOWED_FILES

    @staticmethod
    def upload_file(file):
        if not Storage.check_file_ext(file.name):
            raise Exception(f"It is not allowed to upload files that are not of type: {', '.join(ALLOWED_FILES)}")

        file_prefix = uuid.uuid4().hex
        ext = Path(file.name).suffix

        file_name = f"{file_prefix}{ext}"
        file_content = file.read()

        file_io = BytesIO(file_content)
        blob_client = Storage.create_blob_client(file_name)

        blob_client.upload_blob(data=file_io)

        return blob_client
