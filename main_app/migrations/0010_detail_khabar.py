# Generated by Django 5.0.6 on 2024-09-25 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_posthaye_digar'),
    ]

    operations = [
        migrations.CreateModel(
            name='detail_khabar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='photo')),
                ('code', models.IntegerField()),
                ('tozih', models.CharField(max_length=4000, null=True)),
            ],
        ),
    ]
