# Generated by Django 4.2 on 2023-07-13 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0005_alter_article_options_alter_article_index_together'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='News',
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('title',)},
        ),
    ]
