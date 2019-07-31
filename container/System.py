from dependency_injector import providers, containers

from container.Commands import Commands
from container.Parameters import Parameters
from helper.Logger import getConfiguredLogger
from system.Usage import Usage


class System(containers.DeclarativeContainer):
    logger = getConfiguredLogger(Usage.__name__)

    usage = providers.Factory(
        Usage,
        commands=Commands.allCommands,
        logger=logger,
        systemArguments=Parameters.systemArguments,
    )
