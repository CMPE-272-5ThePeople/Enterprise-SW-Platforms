# Generated by Django 3.1.12 on 2021-12-02 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notifications',
            options={'ordering': ('-timestamp',)},
        ),
    ]
