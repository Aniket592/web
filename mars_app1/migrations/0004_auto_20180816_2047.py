# Generated by Django 2.1 on 2018-08-16 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mars_app1', '0003_auto_20180816_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spacians',
            name='age',
            field=models.CharField(max_length=150),
        ),
    ]
