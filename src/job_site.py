from abc import ABC, abstractmethod


class JobSite(ABC):

    @abstractmethod
    def get_vacancies_list(self):
        pass

    @abstractmethod
    def creation_objects(self, response):
        pass


