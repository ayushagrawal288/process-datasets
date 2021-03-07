import abc


class DataOutput(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def commit(self, data: dict):
        raise NotImplementedError("Need to define this method")

    @abc.abstractmethod
    def get_all(self) -> dict:
        raise NotImplementedError("Need to define this method")
