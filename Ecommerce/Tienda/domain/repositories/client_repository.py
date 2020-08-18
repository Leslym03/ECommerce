from Tienda.mappers import AbstractDataMapper
from Tienda.models import ClientModel
from Tienda.domain.entities.client import Client


class ClientRepository(AbstractDataMapper):

    def find_all(self):
        client_models = ClientModel.objects.all()

        client_entities = []
        for client_model in client_models:
            client_entity = self.__load_entity(client_model)
            client_entities.append(client_entity)
        return client_entities

    def find_by_id(self, id):
        client_model = ClientModel.objects.get(idClient=id)
        client = self.__load_entity(client_model)
        return client

    def create(self, client):
        ClientModel(
            idClient=client.get_idClient(),
            first_name=client.get_first(),
            last_name=client.get_last()
        ).save()

    def update(self, client):
        client_model = ClientModel.objects.get(idClient=client.get_idClient())
        client_model.first_name = client.get_first()
        client_model.last_name = client.get_last()
        client_model.save()

    def delete(self, entity):
        pass

    def __load_entity(self, client_model):
        client_entity = Client(
            client_model.idClient,
            Name(client_model.name)
        )
        return client_entity
