# Generated by Django 3.2.2 on 2021-05-31 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_icons'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='icons',
            new_name='icon',
        ),
    ]