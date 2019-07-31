import logging
from json import JSONEncoder

from youtube_dl import YoutubeDL

from fileSystem.FileSystem import FileSystem
from playlist import PlaylistManager
from prefixer.URLPrefixer import URLPrefixer
from updater import Updater


class PlaylistUpdater(Updater):
    fileSystem: FileSystem

    folderName: str

    logger: logging.Logger

    jsonEncoder: JSONEncoder

    playlistManager: PlaylistManager

    youtubeDL: YoutubeDL

    youtubeDLConfigurationOptions: {}

    youtubeURLPrefixer: URLPrefixer

    def __init__(
            self,
            logger: logging.Logger,
            folderName: str,
            jsonEncoder: JSONEncoder,
            playlistManager: PlaylistManager,
            youtubeDLConfigurationOptions: {},
            youtubeURLPrefixer: URLPrefixer,
    ):
        self.fileSystem = FileSystem(folderName)
        self.folderName = folderName
        self.logger = logger
        self.jsonEncoder = jsonEncoder
        self.playlistManager = playlistManager
        self.youtubeDL = YoutubeDL(youtubeDLConfigurationOptions)
        self.youtubeDLConfigurationOptions = youtubeDLConfigurationOptions
        self.youtubeURLPrefixer = youtubeURLPrefixer

    def update(
            self,
            playlistID: str,
            force=False,
    ):
        if self.fileSystem.checkIfPathExists():
            self.fileSystem.createDirectory()

        fileName = f'{playlistID}.json'

        if self.fileSystem.checkIfFileExists(fileName) and not force:
            self.logger.info(
                f'Already having informations for playlist: {playlistID}',
            )

            return

        extractedInformations = self.youtubeDL.extract_info(
            self.youtubeURLPrefixer.prefixUrl(
                playlistID,
            ),
        )

        self.playlistManager.cache[playlistID] = extractedInformations
        self.playlistManager.save(playlistID)
