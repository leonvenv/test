# Generated by Django 4.0.6 on 2022-07-09 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_short_url_shorturls'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shorturls',
            old_name='short_url',
            new_name='ShortUrls',
        ),
    ]
