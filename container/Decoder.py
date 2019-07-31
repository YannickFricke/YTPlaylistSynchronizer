from json import JSONDecoder

from dependency_injector import containers, providers


class Decoder(containers.DeclarativeContainer):
    json = providers.Factory(JSONDecoder)
