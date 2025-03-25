from django.db import models
from store.models import Product, Variation # import the product model from the store app
# Create your models here.

class Cart(models.Model):
   cart_id = models.CharField(max_length=250, blank=True)
   date_added = models.DateField(auto_now_add=True)

   def __str__(self):
       return self.cart_id
   
# class cart item
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __unicode__(self):
        return self.product