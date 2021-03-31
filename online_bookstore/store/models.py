# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Book(models.Model):
    bookid = models.IntegerField(db_column='bookID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=2000, blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', max_length=45, blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(max_length=45, blank=True, null=True)
    category = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    cover_picture = models.CharField(max_length=45, blank=True, null=True)
    year = models.CharField(max_length=45, blank=True, null=True)
    buy_price = models.CharField(max_length=45, blank=True, null=True)
    sell_price = models.CharField(max_length=45, blank=True, null=True)
    edition = models.CharField(max_length=45, blank=True, null=True)
    quantity = models.CharField(max_length=45, blank=True, null=True)
    rating = models.CharField(max_length=45, blank=True, null=True)
    publisher = models.CharField(max_length=45, blank=True, null=True)
    minimum_threshold = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Book'


class Cart(models.Model):
    cart_id = models.IntegerField(primary_key=True)
    user1_user_id = models.ForeignKey('User1', models.DO_NOTHING, default="", db_column='User1_user_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Cart'


class CartHasInventoryBook(models.Model):
    cart_cart = models.OneToOneField(Cart, models.DO_NOTHING, db_column='Cart_cart_id', primary_key=True)  # Field name made lowercase.
    inventory_book_inventory = models.ForeignKey('InventoryBook', models.DO_NOTHING, db_column='Inventory_Book_inventory_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Cart_has_Inventory_Book'
        unique_together = (('cart_cart', 'inventory_book_inventory'),)


class InventoryBook(models.Model):
    inventory_id = models.IntegerField(primary_key=True)
    book_bookid = models.ForeignKey(Book, models.DO_NOTHING, db_column='Book_bookID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Inventory_Book'


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    user1_user_id = models.ForeignKey('User1', models.DO_NOTHING,  default="", db_column='User1_user_id')  # Field name made lowercase.
    paymentCard_card_number = models.ForeignKey('Paymentcard', models.DO_NOTHING, db_column='PaymentCard_card_number')  # Field name made lowercase.
    total = models.CharField(max_length=45, blank=True, null=True)
    promotion_promo = models.ForeignKey('Promotion', models.DO_NOTHING, db_column='Promotion_promo_id')  # Field name made lowercase.
    order_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Order'


class PaymentCard(models.Model):
    card_number = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    cvv = models.IntegerField(blank=True, null=True)
    expiration_date = models.CharField(max_length=45, blank=True, null=True)
    billing_address = models.CharField(max_length=45, blank=True, null=True)
    user1_user_id = models.ForeignKey('User1', models.DO_NOTHING,  default="", db_column='User1_user_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PaymentCard'


class Promotion(models.Model):
    promo_id = models.IntegerField(primary_key=True)
    startdate = models.DateTimeField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Promotion'


class Transaction(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    book_bookid = models.ForeignKey(Book, models.DO_NOTHING,  default="", db_column='Book_bookID')  # Field name made lowercase.
    order_order = models.ForeignKey(Order, models.DO_NOTHING,  default="", db_column='Order_order_id')  # Field name made lowercase.
    quantity = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'Transaction'


class User1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # userID = models.IntegerField(db_column='userID', primary_key=True)  # Field name made lowercase.
    # username = models.CharField(max_length=45,blank=True,null= True)
    # first_name = models.CharField(max_length=45, blank=True, null=True)
    # last_name = models.CharField(max_length=45, blank=True, null=True)
    # email = models.CharField(max_length=45, blank=True, null=True)
    # password = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    usertype = models.CharField(db_column='userType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='Usercol', max_length=45, blank=True, null=True)  # Field name made lowercase.

    # def __str__(self):
    #     return self.user.username

    class Meta:
        managed = True
        db_table = 'User1'

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         User1.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.user1.save()