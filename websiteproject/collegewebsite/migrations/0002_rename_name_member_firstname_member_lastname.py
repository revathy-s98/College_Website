# Generated by Django 4.1.5 on 2023-04-10 08:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('collegewebsite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='member',
            name='lastname',
            field=models.CharField(default=django.utils.timezone.now, max_length=124),
            preserve_default=False,
        ),
    ]
