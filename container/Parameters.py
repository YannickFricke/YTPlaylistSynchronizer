import os
import sys

from dependency_injector import containers


class Parameters(containers.DeclarativeContainer):
    currentWorkingDirectory = os.getcwd()
    defaultDataDirectory = './data/'
    systemArguments = sys.argv
