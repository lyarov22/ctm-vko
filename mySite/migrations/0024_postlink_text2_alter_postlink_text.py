# Generated by Django 4.2 on 2023-07-28 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0023_postlink_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='postlink',
            name='text2',
            field=models.CharField(default=1, max_length=200, verbose_name='Текст(каз)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postlink',
            name='text',
            field=models.CharField(max_length=200, verbose_name='Текст(рус)'),
        ),
    ]