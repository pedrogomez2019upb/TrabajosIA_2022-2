
#-----------Clase de caracteristica ---------

class Caracteristica:

    def __init__(self, name: str):
        self.name = name.strip()

    def is_equal(self, name: str) -> bool:#Determina si una cadena es igual al nombre de la caracteristica

        return self.name.lower() == name.lower().strip()

    def __eq__(self, item):
        if isinstance(item, Caracteristica):
            return self.is_equal(item.name)
        return False