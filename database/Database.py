import logging
from json import JSONDecoder, JSONEncoder

from fileSystem.JSONObjectFileHandler import JSONObjectFileHandler


class Database(JSONObjectFileHandler):
    logger: logging.Logger

    def __init__(
            self,
            logger: logging.Logger,
            jsonDecoder: JSONDecoder,
            jsonEncoder: JSONEncoder,
            fileName: str = 'database.json',
            folderName: str = './data/',

    ):
        """
        Initializes a new database

        :param logger: The logger to use
        :param fileName: The filename of the database file
        :param folderName: The foldername where the database file should exists
        :param jsonDecoder: The json decoder for the JSONObjectFileHandler
        :param jsonEncoder: The json encoder for the JSONObjectFileHandler
        """

        super().__init__(
            fileName,
            folderName,
            logger,
            jsonDecoder,
            jsonEncoder
        )

        self.logger = logger

    def hasEntry(
            self,
            videoID: str,
    ) -> bool:
        """
        Returns true when an entry exists for the given playlist id

        :param videoID: The id of the playlist to check
        :return: True when an entry exists for the given playlist id
        """

        return videoID in self.decodedContent

    def getEntry(
            self,
            videoID: str,
    ) -> {}:
        if not self.hasEntry(videoID):
            return {
                'artist': '',
                'title': '',
            }

        return self.decodedContent[videoID]

    def setEntry(
            self,
            videoID: str,
            artist: str,
            title: str,
    ):
        self.decodedContent[videoID] = {
            'artist': artist,
            'title': title,
        }
