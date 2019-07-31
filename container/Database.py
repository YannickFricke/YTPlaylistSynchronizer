from dependency_injector import providers

from container.Decoder import Decoder
from container.Parameters import Parameters
from database.Database import Database as DatabaseStorage
from helper.Logger import getConfiguredLogger


class Database:
    fileName = 'database.json'

    logger = getConfiguredLogger(DatabaseStorage.__name__)

    database = providers.Singleton(
        DatabaseStorage,
        currentWorkingDirectory=Parameters.currentWorkingDirectory,
        fileName=fileName,
        folderName=Parameters.defaultDataDirectory,
        jsonDecoder=Decoder.json,
        logger=logger,
    )
