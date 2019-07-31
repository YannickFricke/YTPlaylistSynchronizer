from abc import ABC, abstractmethod


class Updater(ABC):
    @abstractmethod
    def update(
            self,
            id: str,
            force=False,
    ):
        pass
