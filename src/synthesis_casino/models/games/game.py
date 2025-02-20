from abc import ABC, abstractmethod

class Game(ABC):
    @abstractmethod
    def play(self):
        pass

    def __init__(self, name: str, id: str, casino: object):
        self.name = name
        self._id = id
        self.casino = casino

    def __str__(self):
        return f"Game: {self.name}, ID: {self._id}, Casino: {self.casino.name}"
    
    def __repr__(self):
            return f"Game(name={self.name}, id={self._id}, casino={self.casino.name})"

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value