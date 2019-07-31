from threading import Thread

from youtube_dl import YoutubeDL

from prefixer.URLPrefixer import URLPrefixer


class VideoDownloaderThread(Thread):
    videoID: str

    youtubeDL: YoutubeDL

    youtubeDLConfig: {}

    youtubeURLPrefixer: URLPrefixer

    def __init__(
            self,
            videoID: str,
            youtubeURLPrefixer: URLPrefixer,
    ):
        super().__init__(
            name=f'VideoDownloader-{videoID}',
        )

        self.videoID = videoID
        self.youtubeDLConfig = {
            'format': 'bestaudio[ext=mp3]/bestaudio',
            'outtmpl': 'loaded/%(id)s.%(ext)s',
            'no_warnings': True,
            'quiet': True,
        }
        self.youtubeURLPrefixer = youtubeURLPrefixer

    def run(self) -> None:
        self.youtubeDL = YoutubeDL(
            self.youtubeDLConfig,
        )

        self.youtubeDL.download([
            self.youtubeURLPrefixer.prefixUrl(
                self.videoID,
            ),
        ])
