# Generated by Django 3.0.7 on 2022-01-05 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_categary_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.IntegerField(max_length=11)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]
