# Generated by Django 4.1.7 on 2023-05-16 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_remove_image_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]