# Generated by Django 2.1.7 on 2019-03-15 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0003_remove_sensor_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='Temp',
            field=models.IntegerField(default=1.0),
            preserve_default=False,
        ),
    ]
