# Generated by Django 4.0 on 2023-01-24 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0004_rename_display1_photos_display1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sermon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('sermon', models.FileField(upload_to='')),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
