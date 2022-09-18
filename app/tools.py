from abc import abstractmethod

class Printer:
    @abstractmethod
    def print_data(self): pass

class DictionaryPrinter(Printer):
    def __init__(self, data: dict):
        self._data = data
    def print_data(self) -> None:
        print('##############################################')
        [print(f' - {key} : {self._data[key]}') for key in self._data.keys()]
        print('##############################################', end='\n\n')
