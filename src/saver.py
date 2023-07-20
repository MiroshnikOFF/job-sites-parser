from abc import ABC, abstractmethod


class Saver(ABC):

    @classmethod
    @abstractmethod
    def save_to_file(cls, vacancies):
        pass

    @classmethod
    @abstractmethod
    def read_from_file(cls):
        pass

    @classmethod
    @abstractmethod
    def clear_file(cls):
        pass

