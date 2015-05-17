# see subscriptions.management.commands.updatefeeds

from raven import Client
from subscriptions.management.commands.updatefeeds import Command as BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        client = Client()
        try:
            super(Command, self).handle(*args, **options)
        except:
            client.captureException()
