# Generated by Django 2.2 on 2021-08-26 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_buddy_app', '0003_otherstrip'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='user_joined',
            field=models.ManyToManyField(related_name='trip_joined', to='trip_buddy_app.User'),
        ),
    ]
