# see phillyleg.management.commands.updatelegfiles

from raven import Client
from phillyleg.management.commands.updatelegfiles import Command as BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        client = Client()
        try:
            super(Command, self).handle(*args, **options)
        except:
            client.captureException()
