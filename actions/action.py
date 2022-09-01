import abc


class Action:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def act(self, agent, env):
        raise NotImplemented
