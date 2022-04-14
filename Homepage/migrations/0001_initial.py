# Generated by Django 2.2 on 2022-04-14 17:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('body', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='SilderSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
    ]
