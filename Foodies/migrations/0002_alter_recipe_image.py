# Generated by Django 4.1 on 2022-08-18 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foodies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
