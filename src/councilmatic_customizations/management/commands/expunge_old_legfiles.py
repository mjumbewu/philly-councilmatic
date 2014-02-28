###############################################################################
# This will collect the latest legislative filings released in the city of
# Philadelphia.
###############################################################################

#will send out daily email for users - first will read all keywords
#create text files, then email text files to all each user subscribed.

from django.core.management.base import BaseCommand, CommandError
import logging
import optparse
import re
import sys

from phillyleg.models import LegFile

log = logging.getLogger('councilmatic')


class Command(BaseCommand):
    help = "Get rid of duplicate legislation from the older city-hosted legistar site."
    option_list = BaseCommand.option_list + (
            optparse.make_option('--dry-run',
                action='store_true',
                dest='dry_run',
                default=False,
                help='Don\' actually make any DB changes'),
            )

    def handle(self, *args, **options):
        dry_run = options['dry_run']

        domain_pattern = re.compile(r'^https?:\/\/.*\.([^.]+\.[^.]+)\/.*$')
        legfiles = LegFile.objects.all().order_by('id')
        prev = prev_id = prev_host = None

        for curr in legfiles:
            should_delete = None
            delete_host = None

            if curr.id == prev_id:
                prev_host = domain_pattern.match(prev.url)
                curr_host = domain_pattern.match(curr.url)

                if prev_host and curr_host:
                    prev_host = prev_host.group(1)
                    curr_host = curr_host.group(1)

                    if 'legistar.com' == prev_host and curr_host != 'legistar.com':
                        should_delete = curr
                        delete_host = curr_host
                    elif 'legistar.com' != prev_host and curr_host == 'legistar.com':
                        should_delete = prev
                        delete_host = prev_host
                        prev = curr
                    else:
                        log.info('Wait, I\'m confused. Both of these have domains %s and %s.' % (curr_host, prev_host))
                        sys.exit(1)

                if should_delete:
                    log.info('Key %s is a duplicate. One has host legistar. One with host %s will be deleted.' % (prev_id, delete_host))
                    if not dry_run:
                        should_delete.delete()
                    should_delete = None

            else:
                prev = curr
                prev_id = curr.id
