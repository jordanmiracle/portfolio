# Generated by Django 3.1.1 on 2021-10-28 11:29

from django.db import migrations, models
import portfolioproject.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=portfolioproject.storage_backends.MediaStorage()),
        ),
    ]
