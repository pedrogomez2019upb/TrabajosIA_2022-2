import tkinter as tk

import Interfaz.consultar_base as consultar_base


class Interfaz(tk.Frame):
    def __init__(self):
        root = tk.Tk()
        super().__init__(root)
        root.geometry('550x120')
        root.title('SE para detección de enfermedades en palmas')
        root.resizable(width=False, height=False)
        self.master = root
        self.pack()

        self.lbl_base = tk.Label(self, text="Sistema Experto Enfermedades en Palmas")
        self.lbl_base.pack(side="top")
        self.lbl_base.config(font=("Helvetica", 24))

        self.txt_consultar = tk.Button(self, text="Consultar", width=50, command=consultar_base.ConsultarBase)
        self.txt_consultar.pack(side="top", padx=5, pady=5)

        self.quit = tk.Button(self, text="SALIR", width=50, fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom", padx=5, pady=5)
