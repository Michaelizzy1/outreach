# Generated by Django 4.0 on 2023-01-24 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0006_rename_title_sermon_topic_sermon_speaker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
