# Generated by Django 2.1 on 2018-08-16 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mars_app1', '0004_auto_20180816_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spacians',
            name='age',
            field=models.PositiveIntegerField(),
        ),
    ]