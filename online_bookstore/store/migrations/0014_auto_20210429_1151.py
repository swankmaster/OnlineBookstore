# Generated by Django 3.1.7 on 2021-04-29 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20210426_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user1_user_id',
            field=models.ForeignKey(db_column='User1_user_id', default='', on_delete=django.db.models.deletion.CASCADE, to='store.user1'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user1_user_id',
            field=models.ForeignKey(db_column='User1_user_id', default='', on_delete=django.db.models.deletion.CASCADE, to='store.user1'),
        ),
    ]
