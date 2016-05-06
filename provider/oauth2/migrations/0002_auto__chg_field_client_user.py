# encoding: utf-8
from south.v2 import SchemaMigration

class Migration(SchemaMigration):

    dependencies = [
        (b'oauth2', '0001_initial'),
    ]
