# Generated by Django 3.0.5 on 2020-04-26 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_news_publishername'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='PublisherName',
            new_name='publisherName',
        ),
    ]
