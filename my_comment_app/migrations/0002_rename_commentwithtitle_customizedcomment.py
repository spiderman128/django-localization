# Generated by Django 4.0 on 2023-02-14 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('sites', '0002_alter_domain_unique'),
        ('my_comment_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommentWithTitle',
            new_name='CustomizedComment',
        ),
    ]