# Generated by Django 2.1.4 on 2019-03-13 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0002_auto_20190313_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='Temp',
        ),
    ]
