# network/management/commands/reindex.py

from django.core.management.base import BaseCommand
from django_elasticsearch_dsl.registries import registry

class Command(BaseCommand):
    help = 'Réindexe les documents Elasticsearch'

    def handle(self, *args, **options):
        for document in registry.get_documents():
            document.init()
        self.stdout.write(self.style.SUCCESS('Les indices Elasticsearch ont été mis à jour'))
