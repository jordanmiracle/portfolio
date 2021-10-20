# Generated by Django 3.1.1 on 2021-10-19 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('url', models.URLField(blank=True)),
                ('code_url', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/portfolioapp/images')),
            ],
        ),
    ]
