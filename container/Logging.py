import logging

from dependency_injector import containers


class Logging(containers.DeclarativeContainer):
    # Set the standard log level to debug
    defaultLogLevel = logging.DEBUG

    # Set the standard log format
    logFormat = '%(asctime)s %(name)-15s %(levelname)-8s %(message)s'
