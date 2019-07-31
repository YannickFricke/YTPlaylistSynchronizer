from abc import ABC, abstractmethod


class Command(ABC):
    commandName: str

    def __init__(
            self,
            commandName: str
    ):
        self.commandName = commandName

    @abstractmethod
    def run(self) -> None:
        pass
