# Generated by Django 4.1.4 on 2023-01-15 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blog_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catagory',
            new_name='Category',
        ),
    ]
