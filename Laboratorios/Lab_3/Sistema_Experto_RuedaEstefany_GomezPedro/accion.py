"""
Interfaz de consola
"""
from experto_general.motor import Motor


# Motor como variable global
motor = Motor()


def get_base_entries():
    return motor.base.entries

