# encoding: utf-8
from south.v2 import SchemaMigration

class Migration(SchemaMigration):

    dependencies = [
        (b'oauth2', '0003_auto__add_field_client_name'),
    ]
