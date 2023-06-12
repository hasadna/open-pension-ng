from django.core.management.base import BaseCommand, CommandError
from importer import models# TODO remove 
from importer.services import xsls_ingester

class Command(BaseCommand):
    help = "gggxxx"
    # Take filename
    # open using open()
    # pass filestream to xls_ingester
    # print / save:wq


    def add_arguments(self, parser):
        parser.add_argument("mode",  type=str)
        parser.add_argument("path",  type=str)

    def handle(self, *args, **options):
            p=options["path"]
            m=options["mode"]
            self.stdout.write("About to import files from %s" %options["path"])
            xsls_ingester.xls_import(p, None)
            self.stdout.write(
                    self.style.SUCCESS('Successfully imported  "%s"' %options )
            )

