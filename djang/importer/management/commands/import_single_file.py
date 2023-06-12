from django.core.management.base import BaseCommand, CommandError
from importer import models# TODO remove 
from importer import xsls_ingester

class Command(BaseCommand):
    help = "gggxxx"
    # Take filename
    # open using open()
    # pass filestream to xls_ingester
    # print / save:wq


    def add_arguments(self, parser):
        parser.add_argument("mode",  type=str)
        parser.add_argument("file",  type=str)

    def handle(self, *args, **options):
            f=options["file"]
            m=options["mode"]
            xsls_ingester.xls_import(None, f)
            self.stdout.write(
                    self.style.SUCCESS('Successfully imported  "%s"' %options )
            )

