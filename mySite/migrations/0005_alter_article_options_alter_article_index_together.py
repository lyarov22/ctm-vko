# Generated by Django 4.2 on 2023-07-13 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0004_alter_article_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AlterIndexTogether(
            name='article',
            index_together={('id', 'slug')},
        ),
    ]