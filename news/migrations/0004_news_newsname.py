# Generated by Django 3.0.5 on 2020-04-22 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200422_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='newsName',
            field=models.CharField(default='#', max_length=300),
        ),
    ]
