# Generated by Django 5.0.2 on 2024-04-12 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transcript_generator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlepost',
            old_name='video_link',
            new_name='youtube_link',
        ),
        migrations.RenameField(
            model_name='articlepost',
            old_name='video_title',
            new_name='youtube_title',
        ),
    ]