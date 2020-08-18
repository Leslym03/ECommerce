class OrderCompleted(object):

    def __init__(self, order):
        self.order = order


class GenerateInvoice(OrderCompleted):

    def __init__(self):
        pass

    def run(self):
        pass


class RemoveProductFromInventory(OrderCompleted):

    def __init__(self):
        pass

    def run(self):
        pass
