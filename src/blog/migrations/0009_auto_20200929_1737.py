# Generated by Django 2.2 on 2020-09-29 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
