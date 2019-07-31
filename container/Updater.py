from dependency_injector import containers, providers

from container.Encoder import Encoder
from container.Playlist import Playlists
from container.Prefixer import Prefixer
from container.helper import getDataDirectory
from helper.Logger import getConfiguredLogger
from updater.PlaylistUpdater import PlaylistUpdater


class Updater(containers.DeclarativeContainer):
    logger = getConfiguredLogger(PlaylistUpdater.__name__)

    playlistPath = getDataDirectory('playlists')

    playlistUpdater = providers.Factory(
        PlaylistUpdater,
        logger=logger,
        folderName=playlistPath,
        jsonEncoder=Encoder.json,
        playlistManager=Playlists.playlistManager,
        youtubeDLConfigurationOptions={
            'dump_single_json': True,
            'simulate': True,
        },
        youtubeURLPrefixer=Prefixer.youtubePlaylistPrefixer,
    )
