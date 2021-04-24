# Generated by Django 3.1.7 on 2021-04-24 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_order_processed'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('book_bookid', models.ForeignKey(db_column='Book_bookID', on_delete=django.db.models.deletion.DO_NOTHING, to='store.book')),
                ('order_id', models.ForeignKey(db_column='Order.order_id', on_delete=django.db.models.deletion.DO_NOTHING, to='store.order')),
            ],
            options={
                'db_table': 'OrderedBook',
                'managed': True,
            },
        ),
    ]
