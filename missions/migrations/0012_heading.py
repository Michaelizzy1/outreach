# Generated by Django 4.0 on 2023-04-04 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0011_rename_flyer_event_flier_alter_event_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Heading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('url_name', models.CharField(max_length=20)),
            ],
        ),
    ]