# Generated by Django 5.0.6 on 2024-09-25 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_khabar_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='posthaye_digar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='photo')),
                ('code', models.IntegerField()),
                ('rooz', models.IntegerField(default=1)),
                ('sal', models.IntegerField(default=1403)),
                ('mah', models.CharField(max_length=15, null=True)),
                ('safhekhabar', models.CharField(max_length=15, null=True)),
            ],
        ),
    ]
