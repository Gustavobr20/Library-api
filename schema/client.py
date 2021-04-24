from ma import ma
from models.client import ClientModel


class ClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ClientModel
        load_instance = True
