# Generated by Django 2.2 on 2021-08-26 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip_buddy_app', '0004_trip_user_joined'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otherstrip',
            old_name='created_at',
            new_name='other_created_at',
        ),
        migrations.RenameField(
            model_name='otherstrip',
            old_name='destination',
            new_name='other_destination',
        ),
        migrations.RenameField(
            model_name='otherstrip',
            old_name='end_date',
            new_name='other_end_date',
        ),
        migrations.RenameField(
            model_name='otherstrip',
            old_name='plan',
            new_name='other_plan',
        ),
        migrations.RenameField(
            model_name='otherstrip',
            old_name='start_date',
            new_name='other_start_date',
        ),
        migrations.RenameField(
            model_name='otherstrip',
            old_name='updated_at',
            new_name='other_updated_at',
        ),
    ]
