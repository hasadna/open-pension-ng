from django.core.management.base import BaseCommand, CommandError
from importer import models# TODO remove 
from importer.services import xsls_ingester
import os
import io

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
            files = os.listdir(p)
            files = [os.path.join(p, f) for f in files if not f.startswith(".")]
            for filename in files:
                with io.open(filename, "rb") as file:
                    xls = io.BufferedReader(file)
                    ingester = xsls_ingester.xls_ingester()
                    self.stdout.write("ingest %s" %filename )
                    ingester.ingest(filename, xls)
            #xsls_ingester.xls_import(p, None)
            self.stdout.write(
                    self.style.SUCCESS('Successfully imported  "%s"' %options )
            )

