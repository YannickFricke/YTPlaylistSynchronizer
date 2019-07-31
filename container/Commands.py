from dependency_injector import containers, providers

from commands.run import RunCommand
from commands.update import UpdateCommand
from container import Playlist
from container.Parameters import Parameters
from container.Settings import Settings
from container.Updater import Updater
from helper.Logger import getConfiguredLogger


class Commands(containers.DeclarativeContainer):
    runCommand = providers.Factory(
        RunCommand,
        currentWorkingDir=Parameters.currentWorkingDirectory,
        logger=getConfiguredLogger(RunCommand.__name__),
        playlistManager=Playlist.Playlists.playlistManager,
        playlistUpdater=Updater.playlistUpdater,
        settings=Settings.settings,
    )

    updateCommand = providers.Factory(
        UpdateCommand,
        logger=getConfiguredLogger(UpdateCommand.__name__),
        playlistManager=Playlist.Playlists.playlistManager,
        playlistUpdater=Updater.playlistUpdater,
        settings=Settings.settings,
        systemArguments=Parameters.systemArguments,
    )

    allCommands = [
        runCommand(),
        updateCommand(),
    ]
