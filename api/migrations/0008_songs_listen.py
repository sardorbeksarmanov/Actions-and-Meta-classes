# Generated by Django 5.1 on 2024-08-15 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_albom_image_alter_songs_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='listen',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
