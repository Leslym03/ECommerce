from Tienda.mappers import AbstractDataMapper
from Tienda.models import OrderModel
from Tienda.domain.entities.order import Order


class OrderRepository(AbstractDataMapper):

    def find_all(self):
        order_models = OrderModel.objects.all()

        order_entities = []
        for order_model in order_models:
            order_entity = self.__load_entity(order_model)
            order_entities.append(order_entity)
        return order_entities

    def find_by_id(self, id):
        pass

    def create(self, order):
        ProdcutModel(
            product_id=order.get_idProduct(),
            client_id=order.get_idCliente(),
            payment=order.get_payment(),
            state=product.set_state(),
            ordered_date=product.get_ordered_date()
        ).save()

    def update(self, order):
    	order_model.product_id = ProductModel.objects.get(idProduct=product.get_idProduct())
    	order_model.client_id = ClientModel.objects.get(idCliente=client.get_idClient())
        order_model.payment = order.get_payment()
        order_model.state = order.set_state()
        order_model.ordered_date = order.get_ordered_date()
        order_model.save()

    def delete(self, entity):
        pass

    def __load_entity(self, order_model):
        order_entity = Order(
        	order_model.product_id,
            order_model.client_id,
            order_model.payment,
            order_model.state,
            order_model.ordered_date
        )
        return order_entity