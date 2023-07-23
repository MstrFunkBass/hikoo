from storages.backends.azure_storage import AzureStorage
import environ

env = environ.Env()

environ.Env.read_env()

class AzureMediaStorage(AzureStorage):
    account_name = 'hikoodls' # Must be replaced by your <storage_account_name>
    account_key = env('AZURESTORAGEKEY') # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'hikoodls' # Must be replaced by your storage_account_name
    account_key = env('AZURESTORAGEKEY') # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None