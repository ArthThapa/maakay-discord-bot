# Generated by Django 3.2.7 on 2021-09-22 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maakay', '0011_usertip_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertip',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
