# see subscriptions.management.commands.sendfeedupdates

from raven import Client
from subscriptions.management.commands.sendfeedupdates import Command as BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        client = Client()
        try:
            super(Command, self).handle(*args, **options)
        except:
            client.captureException()
