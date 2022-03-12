from unicodedata import decimal

from decimal import Decimal 
from django.conf import settings
from magshop.models import Product

class Cart(object):
    def __init(self,request):
        #Initialize cart
        self.session =request
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            #save empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self.=, product, quantity=1, override_quantity=False):
        #Add a product to the cart or update its quantity.

        product_id=str(product.id)
        if product_id not in self.cart:
            self.cart[product.id]