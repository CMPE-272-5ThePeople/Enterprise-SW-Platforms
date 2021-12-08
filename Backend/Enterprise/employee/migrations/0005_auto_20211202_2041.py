# Generated by Django 3.1.12 on 2021-12-02 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_training'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='training',
            options={'ordering': ['name', 'created'], 'verbose_name': 'Training', 'verbose_name_plural': 'Training'},
        ),
        migrations.AddField(
            model_name='employee',
            name='training',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.training', verbose_name='Training'),
        ),
        migrations.AlterField(
            model_name='training',
            name='total_time',
            field=models.IntegerField(default=1),
        ),
    ]