# Generated by Django 3.0.5 on 2020-04-23 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200422_0141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main',
            old_name='name',
            new_name='titleName',
        ),
        migrations.AddField(
            model_name='main',
            name='imageName',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='main',
            name='imageUrl',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='main',
            name='about',
            field=models.TextField(default='#'),
        ),
    ]
