from src.json_saver import JsonSaver


class Vacancy(JsonSaver):

    all = []

    def __init__(self, all_data, resource, name, city, url, date_time, salary_from, salary_to, currency, requirement):
        self.all_data = all_data
        self.resource = resource
        self.name = name
        self.city = city
        self.url = url
        self.date_time = date_time
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.requirement = requirement
        Vacancy.all.append(self)

    def creation_salary_string(self):
        if self.salary_from and self.salary_to:
            salary_string = f"Зарплата от {self.salary_from} до {self.salary_to}"
        elif self.salary_from and not self.salary_to:
            salary_string = f"Зарплата от {self.salary_from}"
        elif self.salary_to and not self.salary_from:
            salary_string = f"Зарплата до {self.salary_to}"
        elif not self.salary_from and not self.salary_to:
            salary_string = "Зарплата не указана"
        if self.currency:
            salary_string += f" {self.currency}"
        return salary_string

    def __str__(self):
        return f"{self.name}\n{self.city}\n{self.creation_salary_string()}\n" \
               f"Требования: {self.requirement}\n" \
               f"Дата и время размещения: {self.date_time.strftime('%d.%m.%Y %H:%M:%S')}\n" \
               f"URL: {self.url}\n\n################################################################################\n"

    @classmethod
    def get_vacancies_by_salary_from(cls, vacancies, salary_from):
        vacancies_by_salary_from = []
        for vacancy in vacancies:
            if vacancy.salary_from:
                if vacancy.salary_from >= salary_from:
                    vacancies_by_salary_from.append(vacancy)
        return vacancies_by_salary_from

    @classmethod
    def get_vacancies_by_salary_to(cls, vacancies, salary_to):
        vacancies_by_salary_to = []
        for vacancy in vacancies:
            if vacancy.salary_to:
                if vacancy.salary_to <= salary_to:
                    vacancies_by_salary_to.append(vacancy)
        return vacancies_by_salary_to

    @classmethod
    def sort_by_salary(cls, vacancies):
        objects_for_sort = {}
        ascending = []
        descending = []
        for vacancy in vacancies:
            if vacancy.salary_from:
                objects_for_sort[vacancy.salary_from] = vacancy
        objects_sorted = dict(sorted(objects_for_sort.items()))
        for value in objects_sorted.values():
            ascending.append(value)
        objects_sorted_reverse = dict(sorted(objects_for_sort.items(), reverse=True))
        for value in objects_sorted_reverse.values():
            descending.append(value)
        sorted_dict = {}
        sorted_dict['ascending'] = ascending
        sorted_dict['descending'] = descending
        return sorted_dict

    @classmethod
    def sort_by_date(cls, vacancies):
        objects_for_sort = {}
        ascending = []
        descending = []
        for vacancy in vacancies:
            if vacancy.date_time:
                objects_for_sort[vacancy.date_time] = vacancy
        objects_sorted = dict(sorted(objects_for_sort.items()))
        for value in objects_sorted.values():
            ascending.append(value)
        objects_sorted_reverse = dict(sorted(objects_for_sort.items(), reverse=True))
        for value in objects_sorted_reverse.values():
            descending.append(value)
        sorted_dict = {}
        sorted_dict['ascending'] = ascending
        sorted_dict['descending'] = descending
        return sorted_dict




