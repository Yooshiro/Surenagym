# Generated by Django 5.0.6 on 2024-09-23 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_khabar_mah_khabar_rooz'),
    ]

    operations = [
        migrations.AddField(
            model_name='khabar',
            name='sal',
            field=models.IntegerField(default=1403),
        ),
    ]
