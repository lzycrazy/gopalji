# Generated by Django 3.0.7 on 2021-12-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_auto_20211228_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]