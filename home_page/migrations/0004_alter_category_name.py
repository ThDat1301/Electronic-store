# Generated by Django 4.1.7 on 2023-02-28 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0003_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
