from address import Address


class Client(object):

    def __init__(self, idClient, name, last_name):
        self.set_idClient(idClient)
        self.name = Name(name, last_name)
        self.shipping_address = None

    def set_idClient(self, idClient):
        self.idClient = idClient

    def get_idClient(self):
        return self.idClient

    def new_shipping_address(self, street, number, city):
        self.shipping_address = Address(street, number, city)


class Name(object):  
    def __init__(self, first, last):
        self.set_first(first)
        self.set_last(last)

    def set_first(self, first):
        self.first = first

    def get_first(self):
        return self.first

    def set_last(self, last):
        self.last = last

    def get_last(self):
        return self.last

    @property
    def full(self):
        return self.name + self.last_name
