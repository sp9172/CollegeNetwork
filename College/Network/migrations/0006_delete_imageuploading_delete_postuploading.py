# Generated by Django 4.0 on 2022-07-21 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Network', '0005_imageuploading_postuploading_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ImageUploading',
        ),
        migrations.DeleteModel(
            name='PostUploading',
        ),
    ]