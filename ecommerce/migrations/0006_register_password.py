# Generated by Django 3.0.7 on 2022-01-06 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='password',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
