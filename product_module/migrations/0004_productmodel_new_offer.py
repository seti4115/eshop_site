# Generated by Django 4.2.15 on 2024-08-21 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0003_alter_productmodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='new_offer',
            field=models.BooleanField(default=False),
        ),
    ]
