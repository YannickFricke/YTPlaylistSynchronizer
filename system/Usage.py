import logging
from typing import List

from commands import Command
from container.Commands import Commands
from container.Parameters import Parameters


class Usage:
    commands: List[Command]

    scriptFileName: str

    logger: logging.Logger

    def __init__(
            self,
            logger: logging.Logger,
            commands: List[Command] = Commands.allCommands,
            systemArguments: List[str] = Parameters.systemArguments,
    ):
        if len(systemArguments) == 0:
            raise Exception('Systemarguments are emtpy')

        # Set the commands
        self.commands = commands

        # Set the script file name based from the system arguments
        self.scriptFileName = systemArguments[0]

        # Set the logger
        self.logger = logger

    def displayUsage(self):
        self.logger.info(
            f'{self.scriptFileName} - Usage informations',
        )
        self.logger.info(
            'Available commands:',
        )

        for command in self.commands:
            self.logger.info(
                f'- {command.commandName}',
            )
