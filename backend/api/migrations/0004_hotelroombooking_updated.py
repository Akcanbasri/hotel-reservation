# Generated by Django 5.0.1 on 2024-01-29 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_hotelroombooking_remove_hotelroom_check_in_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelroombooking',
            name='updated',
            field=models.BooleanField(default=False),
        ),
    ]