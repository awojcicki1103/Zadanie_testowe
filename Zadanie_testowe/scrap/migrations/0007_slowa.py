# Generated by Django 2.0.7 on 2018-07-31 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0006_delete_slowa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slowa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slowo', models.CharField(max_length=20)),
                ('liczebnosc', models.IntegerField()),
            ],
        ),
    ]
