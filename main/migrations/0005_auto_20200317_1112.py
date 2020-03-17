# Generated by Django 3.0.2 on 2020-03-17 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200317_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='computingID',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='firstname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='gpa',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='phoneNumber',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='schoolYear',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
