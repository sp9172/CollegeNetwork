# Generated by Django 4.0 on 2022-07-21 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Network', '0004_postimageuploading_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUploading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='PostUploading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='PostImageUploading',
        ),
    ]
