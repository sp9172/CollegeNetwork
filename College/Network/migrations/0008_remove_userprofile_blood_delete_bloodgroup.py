# Generated by Django 4.0 on 2022-09-24 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Network', '0007_imageuploading_postuploading'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='blood',
        ),
        migrations.DeleteModel(
            name='bloodgroup',
        ),
    ]
