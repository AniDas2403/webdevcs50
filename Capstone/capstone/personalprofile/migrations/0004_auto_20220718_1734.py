# Generated by Django 3.0.8 on 2022-07-18 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalprofile', '0003_workexp_mt'),
    ]

    operations = [
        migrations.AddField(
            model_name='proj',
            name='duration',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proj',
            name='mt',
            field=models.CharField(default=1, max_length=20480),
            preserve_default=False,
        ),
    ]
