# Generated by Django 3.1.7 on 2021-04-12 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_picture',
            field=models.ImageField(upload_to='static/store/images/'),
        ),
    ]
