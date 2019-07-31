import logging
from json import JSONDecoder, JSONEncoder

from fileSystem.FileHandler import FileHandler


class JSONObjectFileHandler(FileHandler):
    decodedContent: {}

    jsonDecoder: JSONDecoder

    jsonEncoder: JSONEncoder

    logger: logging.Logger

    def __init__(
            self,
            fileName: str,
            folderName: str,
            logger: logging.Logger,
            jsonDecoder: JSONDecoder,
            jsonEncoder: JSONEncoder
    ):
        super().__init__(
            fileName,
            folderName,
        )
        self.logger = logger
        self.jsonDecoder = jsonDecoder
        self.jsonEncoder = jsonEncoder

    def read(self):
        self.logger.debug(
            f'Reading json file: {self.realPath}'
        )

        if not self.fileSystem.checkIfPathExists():
            self.logger.debug(
                f'Directory "{self.folderName}" does not exists. Creating it.'
            )

            self.fileSystem.createDirectory()

        if not self.fileSystem.checkIfFileExists(self.fileName):
            self.fileHandle.write_text('{}')

        fileContents = self.fileHandle.read_text()

        self.decodedContent = self.jsonDecoder.decode(
            fileContents,
        )

    def save(self):
        self.logger.debug(
            f'Saving json file: {self.realPath}'
        )

        if not self.fileSystem.checkIfPathExists():
            self.logger.debug(
                f'Directory "{self.folderName}" does not exists. Creating it.'
            )

            self.fileSystem.createDirectory()

        fileContents = self.jsonEncoder.encode(
            self.decodedContent,
        )

        self.fileHandle.write_text(
            fileContents,
        )
