# Generated by Django 3.0.6 on 2020-09-29 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200929_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.CharField(max_length=64),
        ),
    ]
