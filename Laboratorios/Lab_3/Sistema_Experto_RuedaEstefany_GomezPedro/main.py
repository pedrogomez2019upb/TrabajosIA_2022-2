#------Sistema Experto-------
import Interfaz.menu as menu
from accion import motor

def main():
    motor.base.from_json("enfermedades_palmas.json")  # Por defecto
    app = menu.Interfaz()
    app.mainloop()


if __name__ == '__main__':
    main()
