"""
Django command wait for db to be avalible
"""
from pickle import TRUE
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError

import time

from psycopg2 import OperationalError as Psycopg2OpError


class Command(BaseCommand):
    """ Django command to wait for database"""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = TRUE
            except(Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavalible, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
