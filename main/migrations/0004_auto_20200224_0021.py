# Generated by Django 3.0.2 on 2020-02-24 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200224_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='rating',
            field=models.IntegerField(),
        ),
    ]