import abc


class Simulation:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def run(self, num_of_time_steps: int):
        raise NotImplemented
