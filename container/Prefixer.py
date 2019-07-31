from dependency_injector import containers, providers

from prefixer.URLPrefixer import URLPrefixer


class Prefixer(containers.DeclarativeContainer):
    baseurl = 'https://youtube.com/watch?'
    playlistPrefix = f'{baseurl}list='
    videoPrefix = f'{baseurl}v='

    youtubePlaylistPrefixer = providers.Factory(
        URLPrefixer,
        playlistPrefix,
    )
    youtubeVideoPrefixer = providers.Factory(
        URLPrefixer,
        videoPrefix,
    )
