# Generated by Django 4.2.15 on 2024-09-02 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettingmodel',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]