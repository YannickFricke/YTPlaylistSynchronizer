import os

from container.Parameters import Parameters


def getDataDirectory(directoryName: str) -> str:
    return os.path.join(
        Parameters.defaultDataDirectory,
        directoryName,
    ) + '/'
