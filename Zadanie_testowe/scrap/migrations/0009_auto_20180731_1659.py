# Generated by Django 2.0.7 on 2018-07-31 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0008_auto_20180731_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='text',
            old_name='text',
            new_name='slowo',
        ),
    ]