# Generated by Django 3.1.12 on 2021-12-01 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=999)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
