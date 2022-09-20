from typing import List
from experto_general.caracteristica import Caracteristica


class Entrada:

    def __init__(self, name: str):#Crea una entrada vacía de la base de conocimientos
        self.properties: List[Caracteristica] = []
        self.name = name.strip()
        self.description = ""

    def get_or_add_prop(self, name: str) -> Caracteristica:
        for prop in self.properties:
            if prop.is_equal(name):
                return prop

        prop = Caracteristica(name)
        self.properties.append(prop)
        return prop

    def is_equal(self, name: str) -> bool:#Determina si una cadena es igual al nombre de la entrada
        return self.name.lower() == name.lower().strip()

    def __str__(self):
        res = f'Entry "{self.name}":'
        if len(self.description) > 0:
            res += f"\n\t{self.description}"
        for prop in self.properties:
            res += f"\n\t- {prop.name}"
        return res
