# Generated by Django 4.0 on 2023-01-26 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0009_rename_display1_photos_display_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('venue', models.CharField(max_length=200)),
                ('flyer', models.ImageField(upload_to='')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
