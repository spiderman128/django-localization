# Generated by Django 4.1.6 on 2023-02-13 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_news_alter_page_slug_alter_page_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelTable(
            name='news',
            table='news',
        ),
    ]