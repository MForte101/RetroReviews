# Generated by Django 3.0.5 on 2020-05-01 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
