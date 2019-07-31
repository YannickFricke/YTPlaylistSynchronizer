import logging
from json import JSONDecoder, JSONEncoder
from typing import List

from container.Parameters import Parameters
from fileSystem.JSONObjectFileHandler import JSONObjectFileHandler


class Settings(JSONObjectFileHandler):
    playlists: List[str]

    def __init__(
            self,
            logger: logging.Logger,
            jsonDecoder: JSONDecoder,
            jsonEncoder: JSONEncoder,
    ):
        super().__init__(
            fileName='settings.json',
            folderName=Parameters.defaultDataDirectory,
            jsonDecoder=jsonDecoder,
            jsonEncoder=jsonEncoder,
            logger=logger,
        )

        self.playlists = []

    def initAttributes(self):
        if 'playlists' not in self.decodedContent:
            self.decodedContent['playlists'] = []

        self.playlists = self.decodedContent['playlists']
