from dependency_injector import containers, providers

from container.Decoder import Decoder
from container.Encoder import Encoder
from container.helper import getDataDirectory
from helper.Logger import getConfiguredLogger
from playlist import PlaylistManager


class Playlists(containers.DeclarativeContainer):
    defaultFolderName = getDataDirectory('playlists')

    playlistManager = providers.Singleton(
        PlaylistManager,
        folderName=defaultFolderName,
        logger=getConfiguredLogger(PlaylistManager.__name__),
        jsonDecoder=Decoder.json,
        jsonEncoder=Encoder.json,
    )
