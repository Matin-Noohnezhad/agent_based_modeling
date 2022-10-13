import abc


class Agent:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abc.abstractmethod
    def perceive(self, env):
        raise NotImplemented

    @abc.abstractmethod
    def act(self, env):
        raise NotImplemented
