# Generated by Django 4.2.15 on 2024-09-05 17:22

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0004_productmodel_new_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
