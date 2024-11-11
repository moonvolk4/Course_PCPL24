from abc import ABC, abstractmethod


class geo_figure(ABC):

    @abstractmethod
    def area(self):
        pass