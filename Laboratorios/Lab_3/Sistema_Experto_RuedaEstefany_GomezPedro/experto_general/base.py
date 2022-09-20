from typing import List
from experto_general.entrada import Entrada
from io import open
import json


JSON_LATEST = 1

#-----------------Clase de la base de conocimientos del sistema experto-------------

class BaseConocimientos:

    def __init__(self):#Base de conocimeintos vacia
        self.entries: List[Entrada] = []
        self.description = "Base de conocimientos"

    def from_json(self, filename: str):#Carga una base de conocimientos a partir de un archivo .json
        with open(filename, 'r', encoding='utf8') as f:
            data = f.read()
        obj = json.loads(data)
        self.description = obj['description']
        for json_entry in obj['entries']:
            entry = self.get_or_add_entry(str(json_entry['name']))
            entry.description = str(json_entry['description'])
            for json_prop in json_entry['props']:
                entry.get_or_add_prop(str(json_prop))
        return self

    def get_or_add_entry(self, name: str):
        for entry in self.entries:
            if entry.is_equal(name):
                return entry

        entry = Entrada(name)
        self.entries.append(entry)
        return entry

    def __str__(self):#Mostrar la base como una cadena
        res = f"[{self.description}]"
        for entry in self.entries:
            res += f"\n{entry}\n"
        return res
