class Address(object):

    def __init__(self, street, number, city):
        self.set_street(street)
        self.set_number(number)
        self.set_city(city)

    def set_street(self, street):
        self.street = street

    def set_number(self, street):
        self.number = number

    def set_city(self, city):
        self.city = city

    def get_street(self):
        return self.street

    def get_number(self):
        return self.number

    def get_city(self):
        return self.city