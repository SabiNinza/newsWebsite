# Generated by Django 3.0.5 on 2020-04-21 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200422_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='name',
            field=models.CharField(default='#', max_length=100),
        ),
    ]
