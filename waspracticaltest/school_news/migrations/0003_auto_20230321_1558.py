# Generated by Django 2.1.5 on 2023-03-21 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_news', '0002_auto_20230321_1542'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News',
            new_name='Article',
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': 'Articles'},
        ),
    ]
