# Generated by Django 4.2 on 2023-06-04 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importer', '0005_rename_report_id_assetdetails_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='file_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='reports',
            name='ingested_at',
            field=models.DateField(null=True),
        ),
    ]
