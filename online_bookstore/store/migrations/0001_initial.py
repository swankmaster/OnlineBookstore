# Generated by Django 3.1.7 on 2021-03-29 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookid', models.IntegerField(db_column='bookID', primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=45, null=True)),
                ('isbn', models.CharField(blank=True, db_column='ISBN', max_length=45, null=True)),
                ('author', models.CharField(blank=True, max_length=45, null=True)),
                ('category', models.CharField(blank=True, max_length=45, null=True)),
                ('description', models.CharField(blank=True, max_length=45, null=True)),
                ('cover_picture', models.CharField(blank=True, max_length=45, null=True)),
                ('year', models.CharField(blank=True, max_length=45, null=True)),
                ('buy_price', models.CharField(blank=True, max_length=45, null=True)),
                ('sell_price', models.CharField(blank=True, max_length=45, null=True)),
                ('edition', models.CharField(blank=True, max_length=45, null=True)),
                ('quantity', models.CharField(blank=True, max_length=45, null=True)),
                ('rating', models.CharField(blank=True, max_length=45, null=True)),
                ('publisher', models.CharField(blank=True, max_length=45, null=True)),
                ('minimum_threshold', models.CharField(blank=True, max_length=45, null=True)),
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
                ('startdate', models.DateTimeField(blank=True, db_column='startDate', null=True)),
                ('enddate', models.DateTimeField(blank=True, db_column='endDate', null=True)),
                ('discount', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'Promotion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userid', models.IntegerField(db_column='userID', primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=45, null=True)),
                ('last_name', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.CharField(blank=True, max_length=45, null=True)),
                ('password', models.CharField(blank=True, max_length=45, null=True)),
                ('phone', models.CharField(blank=True, max_length=45, null=True)),
                ('status', models.CharField(blank=True, max_length=45, null=True)),
                ('usertype', models.CharField(blank=True, db_column='userType', max_length=45, null=True)),
                ('userscol', models.CharField(blank=True, db_column='Userscol', max_length=45, null=True)),
            ],
            options={
                'db_table': 'Users',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity', models.CharField(max_length=45)),
                ('book_bookid', models.ForeignKey(db_column='Book_bookID', on_delete=django.db.models.deletion.DO_NOTHING, to='store.book')),
                ('order_order', models.ForeignKey(db_column='Order_order_id', on_delete=django.db.models.deletion.DO_NOTHING, to='store.order')),
            ],
            options={
                'db_table': 'Transaction',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Paymentcard',
            fields=[
                ('card_number', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=45, null=True)),
                ('expiration_date', models.CharField(blank=True, max_length=45, null=True)),
                ('billing_address', models.CharField(blank=True, max_length=45, null=True)),
                ('users_userid', models.ForeignKey(db_column='Users_userID', on_delete=django.db.models.deletion.DO_NOTHING, to='store.users')),
            ],
            options={
                'db_table': 'PaymentCard',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='order',
            name='paymentcard_card_number',
            field=models.ForeignKey(db_column='PaymentCard_card_number', on_delete=django.db.models.deletion.DO_NOTHING, to='store.paymentcard'),
        ),
        migrations.AddField(
            model_name='order',
            name='promotion_promo',
            field=models.ForeignKey(db_column='Promotion_promo_id', on_delete=django.db.models.deletion.DO_NOTHING, to='store.promotion'),
        ),
        migrations.AddField(
            model_name='order',
            name='users_userid',
            field=models.ForeignKey(db_column='Users_userID', on_delete=django.db.models.deletion.DO_NOTHING, to='store.users'),
        ),
        migrations.CreateModel(
            name='InventoryBook',
            fields=[
                ('inventory_id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_bookid', models.ForeignKey(db_column='Book_bookID', on_delete=django.db.models.deletion.DO_NOTHING, to='store.book')),
            ],
            options={
                'db_table': 'Inventory_Book',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.IntegerField(primary_key=True, serialize=False)),
                ('users_userid', models.ForeignKey(db_column='Users_userID', on_delete=django.db.models.deletion.DO_NOTHING, to='store.users')),
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
                ('inventory_book_inventory', models.ForeignKey(db_column='Inventory_Book_inventory_id', on_delete=django.db.models.deletion.DO_NOTHING, to='store.inventorybook')),
            ],
            options={
                'db_table': 'Cart_has_Inventory_Book',
                'managed': True,
                'unique_together': {('cart_cart', 'inventory_book_inventory')},
            },
        ),
    ]
