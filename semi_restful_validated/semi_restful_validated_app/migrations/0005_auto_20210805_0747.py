# Generated by Django 2.2 on 2021-08-05 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_restful_validated_app', '0004_auto_20210804_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='show',
            name='network',
            field=models.CharField(max_length=255),
        ),
    ]