# see subscriptions.management.commands.cleanfeeds

from raven import Client
from subscriptions.management.commands.cleanfeeds import Command as BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        client = Client()
        try:
            super(Command, self).handle(*args, **options)
        except:
            client.captureException()
