# Generated by Django 5.0.6 on 2024-09-29 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_akhbar_safhe_khabar_alter_akhbar_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akhbar',
            name='safhe_khabar',
            field=models.CharField(max_length=15, null=True, verbose_name='صفحه خبر'),
        ),
    ]
