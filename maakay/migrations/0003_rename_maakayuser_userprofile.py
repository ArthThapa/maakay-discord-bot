# Generated by Django 3.2.7 on 2021-10-24 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('maakay', '0002_alter_usertip_amount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MaakayUser',
            new_name='UserProfile',
        ),
    ]
