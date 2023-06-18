from django.core.management.base import BaseCommand, CommandError
from importer import models# TODO remove 
from importer.services import xsls_ingester
import io
import os

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
            filename="/home/guyga/hasadna/penssion/xlsx-files/files/רשימת נכסים ברמת נכס בודד- Public - מסלול פנסיה-2020 רבעון 1-מגדל מקפת אישית  למקבלי קצבה קיימים.xlsx"#options["file"]
            m=options["mode"]
            ingester = xsls_ingester.xls_ingester()
            with io.open(filename, "rb") as file:
                    xls = io.BufferedReader(file)
                    ingester = xsls_ingester.xls_ingester()
                    self.stdout.write("ingest %s" %filename )
                    ingester.ingest(filename, xls)
            self.stdout.write(
                    self.style.SUCCESS('Successfully imported  "%s"' %options )
            )

