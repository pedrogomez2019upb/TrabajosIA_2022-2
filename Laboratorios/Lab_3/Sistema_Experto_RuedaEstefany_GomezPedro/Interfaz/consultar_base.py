import tkinter as tk
import tkinter.messagebox as messagebox
from experto_general.respuesta import Respuesta
from accion import motor


class ConsultarBase(tk.Frame):

    def __init__(self):
        self.master = tk.Toplevel()
        super().__init__(self.master)

        self.master.geometry('500x300')
        self.master.title('Consultar al sistema')
        self.master.resizable(width=False, height=False)

        self.lbl_question = tk.Label(self, text="PREGUNTA")
        self.lbl_question.pack(side="top", pady=20)
        self.lbl_question.config(font=("Helvetica", 12))

        self.btn_yes = tk.Button(self, text="Sí", width=20, command=self._send_yes)
        self.btn_yes.pack(side="left", padx=5, pady=5)

        self.btn_no = tk.Button(self, text="No", width=20, command=self._send_no)
        self.btn_no.pack(side="right", padx=5, pady=5)

        self.pack()
        self.questions = motor.generate()
        self._get_question(Respuesta.NO)

    def _send_yes(self):
        self._get_question(Respuesta.YES)

    def _send_no(self):
        self._get_question(Respuesta.NO)

    def _get_question(self, response: Respuesta):
        try:
            motor.set_response(response)
            question = next(self.questions)

            if question is not None:
                self.lbl_question.config(text=f"¿{question.name}?")
            else:
                self._finished()

        except StopIteration:
            self._finished()

    def _finished(self):
        if motor.result is None:
            messagebox.showerror("Error",
                                 "No se encontró ninguna enfermedad que coincida con los sintomas ingresados")
        else:
            reason = f"Síntomas comunes:\n"
            for prop in motor.result.properties:
                reason += f"- {prop.name}\n"
            messagebox.showinfo("Detección",
                                f"Enfermedad: {motor.result.name}\n\n{motor.result.description}\n\n" + reason)

        self.master.destroy()