# Generated by Django 4.2 on 2023-07-18 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0011_remove_post_images_post_image_alter_postimage_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(upload_to='post/%Y/%m/%d/'),
        ),
    ]
