import logging
from typing import List

from commands import Command
from playlist import PlaylistManager
from settings import Settings
from updater.PlaylistUpdater import PlaylistUpdater


class UpdateCommand(Command):
    logger: logging.Logger

    playlistManager: PlaylistManager

    playlistUpdater: PlaylistUpdater

    settings: Settings

    systemArguments: List[str]

    def __init__(
            self,
            logger: logging.Logger,
            playlistManager: PlaylistManager,
            playlistUpdater: PlaylistUpdater,
            settings: Settings,
            systemArguments: List[str],
    ):
        super().__init__(
            'update',
        )

        self.logger = logger
        self.playlistManager = playlistManager
        self.playlistUpdater = playlistUpdater
        self.settings = settings
        self.systemArguments = systemArguments[2:]

    def run(self) -> None:
        self.settings.read()
        self.settings.initAttributes()

        playlists = self.settings.playlists

        if len(self.systemArguments) > 0:
            playlists = self.systemArguments

        self.logger.debug(
            f'Processing the following playlists: {playlists}',
        )

        for playlistID in playlists:
            self.logger.debug(
                f'Updating playlist: {playlistID}'
            )

            self.playlistUpdater.update(
                playlistID,
                True,
            )

            self.logger.debug(
                f'Updated playlist: {playlistID}'
            )
