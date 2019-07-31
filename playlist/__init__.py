import logging
import os
from json import JSONEncoder, JSONDecoder
from pathlib import Path

from fileSystem.FileSystem import FileSystem


class PlaylistManager:
    cache: {}

    fileHandle: Path

    fileName: str

    fileSystem: FileSystem

    folderName: str

    logger: logging.Logger

    jsonDecoder: JSONDecoder

    jsonEncoder: JSONEncoder

    resolvedFilePath: str

    def __init__(
            self,
            folderName: str,
            logger: logging.Logger,
            jsonDecoder: JSONDecoder,
            jsonEncoder: JSONEncoder,
    ):
        self.cache = {}
        self.fileSystem = FileSystem(folderName)
        self.folderName = folderName
        self.logger = logger
        self.jsonDecoder = jsonDecoder
        self.jsonEncoder = jsonEncoder

    def readAllPlaylists(self):
        self.logger.debug(
            'Reading all playlists from the file system',
        )

        if not self.fileSystem.checkIfPathExists():
            self.logger.debug(
                f'Path "{self.folderName}" does not exists. Creating it.',
            )

            self.fileSystem.createDirectory()

        files = os.listdir(self.folderName)

        for file in files:
            self.logger.debug(
                f'Processing file {file}'
            )
            fileParts = file.split('.')
            playlistID = fileParts[0]

            self.read(playlistID)

    def read(
            self,
            playlistID: str,
    ) -> {}:
        self.logger.debug(
            f'Reading playlist with id: {playlistID}',
        )

        if playlistID in self.cache:
            self.logger.debug(
                'Playlist already exists in the cache',
            )
            return self.cache[playlistID]

        fileName = f'{playlistID}.json'
        resolvedFilePath = os.path.join(
            self.folderName,
            fileName,
        )

        self.logger.debug(
            f'Resolved file path: {resolvedFilePath}',
        )

        fileHandle = Path(
            resolvedFilePath,
        )

        fileContents = fileHandle.read_text()
        decodedContents = self.jsonDecoder.decode(
            str(fileContents),
        )

        self.logger.debug(
            f'Set cache contents for playlist: {playlistID}',
        )

        self.cache[playlistID] = decodedContents

        return decodedContents

    def save(
            self,
            playlistID: str,
    ):
        self.logger.debug(
            f'Saving playlist with the id: {playlistID}',
        )

        encodedContents = self.jsonEncoder.encode(
            self.cache[playlistID],
        )

        fileName = f'{playlistID}.json'
        resolvedFilePath = os.path.join(
            self.folderName,
            fileName,
        )

        self.logger.debug(
            f'Resolved file path {resolvedFilePath}',
        )

        fileHandle = Path(
            resolvedFilePath,
        )

        fileHandle.write_text(
            str(encodedContents),
        )

        self.logger.debug(
            f'Wrote file contents for file {resolvedFilePath}',
        )

    def saveAllPlaylists(self):
        self.logger.debug(
            'Saving all playlists',
        )

        for playlistID in self.cache:
            self.logger.debug(
                f'Saving playlist {playlistID}',
            )
            self.save(playlistID)
            self.logger.debug(
                f'Saved playlist {playlistID}',
            )
