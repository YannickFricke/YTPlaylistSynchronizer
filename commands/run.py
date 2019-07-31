import logging
from threading import Thread
from typing import List

from commands import Command
from container.Prefixer import Prefixer
from playlist import PlaylistManager
from settings import Settings
from threads.VideoDownloaderThread import VideoDownloaderThread
from updater.PlaylistUpdater import PlaylistUpdater


class RunCommand(Command):
    currentWorkingDir: str

    logger: logging.Logger

    playlistManager: PlaylistManager

    playlistUpdater: PlaylistUpdater

    settings: Settings

    threads: List[Thread]

    def __init__(
            self,
            currentWorkingDir: str,
            logger: logging.Logger,
            playlistManager: PlaylistManager,
            playlistUpdater: PlaylistUpdater,
            settings: Settings,
    ):
        super().__init__('run')
        self.currentWorkingDir = currentWorkingDir
        self.logger = logger
        self.playlistManager = playlistManager
        self.playlistUpdater = playlistUpdater
        self.settings = settings
        self.threads = []

    def run(self) -> None:
        """
        Runs the run command

        :return: None
        """

        self.logger.info(
            f'In current working directory: {self.currentWorkingDir}',
        )

        self.logger.info(
            'Loading all saved playlists',
        )

        self.playlistManager.readAllPlaylists()

        self.settings.read()
        self.settings.initAttributes()

        if len(self.settings.playlists) == 0:
            self.logger.warning(
                'No playlists found in the settings file.',
            )

            return

        self.fetchPlaylists()

        for playlistID in self.playlistManager.cache:
            self.processPlaylist(playlistID)

        self.startAndAwaitAllThreads()

    def fetchPlaylists(self):
        self.logger.info(
            'Fetching all playlists!',
        )

        for playlistID in self.settings.playlists:
            self.logger.debug(
                f'Fetching playlist: {playlistID}',
            )

            self.playlistUpdater.update(
                playlistID,
            )

            self.logger.debug(
                f'Fetched playlist: {playlistID}',
            )

        self.logger.info(
            'Fetched all playlists!',
        )

    def processPlaylist(
            self,
            playlistID: str,
    ):
        self.logger.debug(
            f'Processing playlist: {playlistID}',
        )

        playlistData = self.playlistManager.cache[playlistID]
        videoIDs = [entry['id'] for entry in playlistData['entries']]

        self.logger.debug(
            f'Found {len(videoIDs)} video ids',
        )

        for videoID in videoIDs:
            self.addVideoDownloaderThread(
                videoID,
            )

    def addVideoDownloaderThread(
            self,
            videoID: str
    ):
        videoDownloaderThread = VideoDownloaderThread(
            videoID,
            Prefixer.youtubeVideoPrefixer(),
        )

        self.threads.append(
            videoDownloaderThread,
        )

    def startAndAwaitAllThreads(self):
        for thread in self.threads:
            index = self.threads.index(thread) + 1
            length = len(self.threads)

            self.logger.info(
                f'Downloading video {index} from {length}',
            )

            thread.start()
            thread.join()

            self.logger.info(
                f'Downloaded video {index} from {length}',
            )
