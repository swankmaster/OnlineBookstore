# Generated by Django 3.1.7 on 2021-04-21 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_cryptography.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookid', models.IntegerField(db_column='bookID', primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=2000, null=True)),
                ('isbn', models.CharField(blank=True, db_column='isbn', max_length=45, null=True)),
                ('author', models.CharField(blank=True, max_length=45, null=True)),
                ('category', models.CharField(blank=True, max_length=45, null=True)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('cover_picture', models.ImageField(blank=True, null=True, upload_to='online_bookstore/store/static/store/images/')),
                ('year', models.IntegerField(blank=True, null=True)),
                ('buy_price', models.FloatField(blank=True, null=True)),
                ('sell_price', models.FloatField(blank=True, null=True)),
                ('edition', models.CharField(blank=True, max_length=45, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('publisher', models.CharField(blank=True, max_length=45, null=True)),
                ('minimum_threshold', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Book',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('total', models.CharField(blank=True, max_length=45, null=True)),
                ('order_datetime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Order',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('promo_id', models.IntegerField(primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField(blank=True, db_column='start_date', null=True)),
                ('end_date', models.DateTimeField(blank=True, db_column='end_date', null=True)),
                ('discount', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'Promotion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=45, null=True)),
                ('receive_promotions', models.BooleanField(default=False)),
                ('status', models.CharField(blank=True, max_length=45, null=True)),
                ('user_suspend', models.BooleanField(db_column='user_suspend', default=False)),
                ('usercol', models.CharField(blank=True, db_column='Usercol', max_length=45, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'User1',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity', models.CharField(max_length=45)),
                ('book_bookid', models.ForeignKey(db_column='Book_bookID', default='', on_delete=django.db.models.deletion.DO_NOTHING, to='store.book')),
                ('order_order', models.ForeignKey(db_column='Order_order_id', default='', on_delete=django.db.models.deletion.DO_NOTHING, to='store.order')),
            ],
            options={
                'db_table': 'Transaction',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PaymentCard',
            fields=[
                ('card_id', models.IntegerField(db_column='PaymentCard_card_id', primary_key=True, serialize=False)),
                ('card_number', django_cryptography.fields.encrypt(models.CharField(max_length=16))),
                ('type', models.CharField(blank=True, max_length=45, null=True)),
                ('cvv', django_cryptography.fields.encrypt(models.IntegerField(blank=True, null=True))),
                ('expiration_date', models.CharField(blank=True, max_length=45, null=True)),
                ('billing_address', models.CharField(blank=True, max_length=45, null=True)),
                ('user1_user_id', models.ForeignKey(db_column='User1_user_id', default='', on_delete=django.db.models.deletion.DO_NOTHING, to='store.user1')),
            ],
            options={
                'db_table': 'PaymentCard',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='order',
            name='paymentCard_card_id',
            field=models.ForeignKey(db_column='PaymentCard_card_id', on_delete=django.db.models.deletion.DO_NOTHING, to='store.paymentcard'),
        ),
        migrations.AddField(
            model_name='order',
            name='promotion_promo',
            field=models.ForeignKey(db_column='Promotion_promo_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='store.promotion'),
        ),
        migrations.AddField(
            model_name='order',
            name='user1_user_id',
            field=models.ForeignKey(db_column='User1_user_id', default='', on_delete=django.db.models.deletion.DO_NOTHING, to='store.user1'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user1_user_id', models.ForeignKey(db_column='User1_user_id', default='', on_delete=django.db.models.deletion.DO_NOTHING, to='store.user1')),
            ],
            options={
                'db_table': 'Cart',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CartHasInventoryBook',
            fields=[
                ('cart_cart', models.OneToOneField(db_column='Cart_cart_id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='store.cart')),
                ('book_bookid', models.ForeignKey(db_column='Book_bookID', on_delete=django.db.models.deletion.DO_NOTHING, to='store.book')),
            ],
            options={
                'db_table': 'Cart_has_Inventory_Book',
                'managed': True,
            },
        ),
    ]
