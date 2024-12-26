from django.core.management.base import BaseCommand, CommandError
from importer import models# TODO remove 
from importer.services import xsls_ingester
from importer.services import ingester_with_calamine
import os
import io
import datetime

class Command(BaseCommand):
    help = "gggxxx"
    # Take filename
    # open using open()
    # pass filestream to xls_ingester
    # print / save:wq


    def add_arguments(self, parser):
        parser.add_argument("mode",  type=str)
        parser.add_argument("path",  type=str)
        parser.add_argument("force_override",nargs='?', 
            help="Overwrite existing reports",)

    def handle(self, *args, **options):
            p=options["path"]
            m=options["mode"]
            
            count = failed = 0
            pyxl = calamine = 0
            self.stdout.write(str(datetime.datetime.now())+" About to import files from %s" %options["path"])
            files = os.listdir(p)
            files = [os.path.join(p, f) for f in files if not f.startswith(".")]
            for filename in files:
                with io.open(filename, "rb") as file:
                    xls = io.BufferedReader(file)
                    ingester = xsls_ingester.xls_ingester()
                    ingester.force = options["force_override"] is not None
                    self.stdout.write("ingest %s" %filename )
                    status=ingester.ingest(filename, xls)
                    if not status:
                        ingester = ingester_with_calamine.Ingester_whith_calamine()
                        self.stdout.write("ingest with calamine %s" %filename )
                        status=ingester.ingest(filename, xls)
                        calamine +=1
                    if status:
                        count +=1
                        self.stdout.write('count={0}'.format(count))
                    else:
                        failed +=1    
            #xsls_ingester.xls_import(p, None)
            self.stdout.write(
                    self.style.SUCCESS(str(datetime.datetime.now())+
                         'Successfully imported {0} files, {1} files failed, {2}'.format(count, failed, calamine))
            )

