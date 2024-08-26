# Generated by Django 4.2.15 on 2024-08-19 14:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=5), django.core.validators.MinValueValidator(limit_value=1)])),
                ('price', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=100), django.core.validators.MinValueValidator(limit_value=0)])),
                ('price_discount', models.FloatField(editable=False)),
                ('urlname', models.SlugField(allow_unicode=True, editable=False, unique=True)),
            ],
        ),
    ]