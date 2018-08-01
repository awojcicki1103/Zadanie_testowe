# Generated by Django 2.0.7 on 2018-07-30 15:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stats',
            name='close',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='open',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='ticker',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='volume',
        ),
        migrations.AddField(
            model_name='stats',
            name='slowo',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]
