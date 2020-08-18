from Tienda.mappers import AbstractDataMapper
from Tienda.models import ProductModel
from Tienda.domain.entities.product import Product


class ProductRepository(AbstractDataMapper):

    def find_all(self):
        product_models = ProductModel.objects.all()

        product_entities = []
        for product_model in product_models:
            product_entity = self.__load_entity(product_model)
            product_entities.append(product_entity)
        return product_entities

    def find_by_id(self, id):
        product_model = ProductModel.objects.get(idProduct=id)
        product = self.__load_entity(product_model)
        return product

    def create(self, product):
        ProdcutModel(
        	idProduct=product.get_idProduct(),
            title=product.get_title(),
            description=product.get_description(),
            price=product.get_price(),
            category=product.get_category(),
            image=product.get_image(),
            slug=product.get_slug()
        ).save()

    def update(self, product):
    	product_model = ProductModel.objects.get(idProduct=product.get_idProduct())
        product_model.title = product.get_title()
        product_model.description = product.get_description()
        product_model.price = product.get_price()
        product_model.category = product.get_category()
        product_model.image = product.get_image()
        product_model.slug = product.get_slug()
        product_model.save()

    def delete(self, entity):
        pass

    def __load_entity(self, product_model):
        product_entity = Product(
        	product_model.idProduct,
            product_model.title,
            product_model.description,
            product_model.price,
            product_model.category,
            product_model.image,
            product_model.slug
        )
        return product_entity
