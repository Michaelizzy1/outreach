# Generated by Django 4.0 on 2023-04-06 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0012_heading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heading',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
