# Generated by Django 5.0.6 on 2024-06-22 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormApp', '0003_remove_detection_detection_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detection',
            name='upload_file',
            field=models.FileField(upload_to='findings/'),
        ),
    ]