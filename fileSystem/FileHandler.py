import os
from abc import ABC
from pathlib import Path

from fileSystem.FileSystem import FileSystem


class FileHandler(ABC):
    fileHandle: Path

    fileName: str

    fileSystem: FileSystem

    folderName: str

    realPath: str

    def __init__(
            self,
            fileName: str,
            folderName: str,
    ):
        self.realPath = os.path.realpath(
            folderName + fileName,
        )

        self.fileHandle = Path(self.realPath)
        self.fileName = fileName
        self.fileSystem = FileSystem(folderName)
        self.folderName = folderName
