# Generated by Django 3.1.2 on 2020-10-07 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='thumpnail',
            new_name='thumbnail',
        ),
    ]
