# Generated by Django 4.1.4 on 2023-01-12 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_catagory_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]
