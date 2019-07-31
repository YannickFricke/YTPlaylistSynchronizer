from json import JSONEncoder

from dependency_injector import containers, providers


class Encoder(containers.DeclarativeContainer):
    json = providers.Factory(JSONEncoder)
