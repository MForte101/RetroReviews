# Generated by Django 3.0.5 on 2020-04-29 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_article_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=100, null=True)),
                ('video_url', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]