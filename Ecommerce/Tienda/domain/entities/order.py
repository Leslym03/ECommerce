from client import Client
from product import Product

class Order(object):

    def __init__(self, product, client, payment, state, ordered_date):
        self.product_id = product.idProducto
        self.client_id = client.idClient
        self.set_payment(payment)
        self.set_state(state)
        self.set_ordered_date(ordered_date)


    def set_payment(self, payment):
    	self.payment = payment

    def set_state(self, state):
    	self.state = state

    def set_ordered_date(self, ordered_date):
    	self.ordered_date = ordered_date



    def get_payment(self):
        return self.payment

    def get_state(self):
        return self.state

    def get_ordered_date(self):
        return self.ordered_date




    