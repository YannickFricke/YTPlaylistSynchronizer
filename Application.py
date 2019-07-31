import logging
import os
from typing import List

from commands import Command
from container.Commands import Commands
from system.Usage import Usage


class Application:
    """
    The application for the YouTube playlist sychronizer
    """

    command: str

    commandArguments: List[str]

    currentDirectory: str

    logger: logging.Logger

    registeredCommands: List[Command]

    systemArguments: List[str]

    usage: Usage

    def __init__(
            self,
            systemArguments: List[str],
            logger: logging.Logger,
            usage: Usage,
    ):
        """
        Initializes a new Application

        :param systemArguments: The system arguments for the application
        :param logger: The logger to use
        """

        self.command = ''
        self.commandArguments = []
        self.currentDirectory = os.getcwd()
        self.logger = logger
        self.registeredCommands = Commands.allCommands
        self.systemArguments = systemArguments
        self.usage = usage

        strippedArguments = systemArguments[1:]

        if len(strippedArguments) > 0:
            self.command = strippedArguments[0]
            self.commandArguments = strippedArguments[1:]

    def run(self):
        # Runs the command when there is any
        # When there is none, the usage will be
        # displayed and exited with status code 1
        if not self.runCommand():
            # Display the usage
            self.usage.displayUsage()

            # Exit with status code one
            exit(1)

    def runCommand(self) -> bool:

        # Check if the command is an empty string
        if self.command.strip(' ') == '':
            # Return false because there is no command to run
            return False

        self.logger.debug(
            f'Trying to run command "{self.command}"'
        )

        # Iterate through all known commands
        for command in self.registeredCommands:
            self.logger.debug(
                f'Processing command: {command.commandName}',
            )

            # Check if the name of the command
            # matches with the own command name
            if command.commandName != self.command:
                # It does not matches so we skip the command

                continue

            self.logger.debug(
                f'Running command: {command.commandName}',
            )

            # Run the command
            command.run()

            # Return true because we found the command and run it
            return True

        # Return false because we didn't found the command
        return False
