# Generated by Django 4.1.7 on 2023-02-28 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0002_user_avatar_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=None, upload_to='home_page/images/collection'),
        ),
    ]
