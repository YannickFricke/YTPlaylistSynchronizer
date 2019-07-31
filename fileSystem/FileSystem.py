import os

from container.Parameters import Parameters


class FileSystem:
    path: str

    def __init__(
            self,
            path: str = Parameters.currentWorkingDirectory,
    ):
        self.path = path

    def checkIfPathExists(self) -> bool:
        """
        Returns true when the path already exists
        :return: True when the path already exists
        """

        return os.path.exists(
            self.path,
        )

    def createDirectory(self) -> None:
        """
        Creates the directory when it not exists

        :return: None
        """

        # Check if the path already exists
        if self.checkIfPathExists():
            # The path already exists so we don't
            # need to create it
            return

        # Create the directory
        os.mkdir(
            self.path,
        )

    def checkIfFileExists(
            self,
            fileName: str,
    ) -> bool:
        """
        Returns true when the file exists

        :param fileName: The name of the file to check
        :return: True when the file exists
        """

        filePath = os.path.realpath(self.path + fileName, )

        return os.path.isfile(
            filePath
        )
