from dependency_injector import containers, providers

from container.Decoder import Decoder
from container.Encoder import Encoder
from helper.Logger import getConfiguredLogger
from settings import Settings as BaseSettings


class Settings(containers.DeclarativeContainer):
    settings = providers.Singleton(
        BaseSettings,
        getConfiguredLogger(BaseSettings.__name__),
        jsonDecoder=Decoder.json,
        jsonEncoder=Encoder.json,
    )
