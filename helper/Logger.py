import logging

from container.Logging import Logging

# Define a standard stream handler
standardStreamHandler: logging.StreamHandler = logging.StreamHandler()

# Define a standard formatter
# with the given log format from the container
standardFormatter: logging.Formatter = logging.Formatter(
    Logging.logFormat,
)

# Set the formatter
standardStreamHandler.setFormatter(standardFormatter)


def getConfiguredLogger(
        name: str,
) -> logging.Logger:
    """
    Returns a configured logger with the given name

    :param name: The name of the logger
    :return: A freshly created logger for the configured name
    """

    # Create a new logger
    logger = logging.getLogger(name)

    # Enhance the logger
    enhancedLogger = applyStandardThingsForLogger(logger)

    # Return the enhanced logger
    return enhancedLogger


def applyStandardThingsForLogger(
        logger: logging.Logger,
) -> logging.Logger:
    """
    Applies standard things onto a logger

    :param logger: The logger to modify
    :return: The modified logger
    """

    # Clone the variable
    result = logger

    # Add the handler to the logger
    result.addHandler(standardStreamHandler)

    # Set the log level to DEBUG
    result.setLevel(Logging.defaultLogLevel)

    # Return the configured logger
    return result
