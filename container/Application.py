from dependency_injector import providers, containers

from Application import Application
from container.Parameters import Parameters
from container.System import System
from helper.Logger import getConfiguredLogger


class Applications(containers.DeclarativeContainer):
    application = providers.Factory(
        Application,
        logger=getConfiguredLogger(Application.__name__),
        systemArguments=Parameters.systemArguments,
        usage=System.usage,
    )
