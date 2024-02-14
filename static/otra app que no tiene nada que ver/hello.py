import tkinter as tk
from tkinter import messagebox
import random

class RandomParticipantSelector:
    def __init__(self, master):
        self.master = master
        self.master.title("Selector Aleatorio de Participantes")

        self.participants = []
        self.selected_participants = []

        self.label = tk.Label(master, text="Ingrese un participante:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.add_button = tk.Button(master, text="Agregar", command=self.add_participant)
        self.add_button.pack()

        self.next_button = tk.Button(master, text="Siguiente", command=self.select_next)
        self.next_button.pack()

        self.reset_button = tk.Button(master, text="Reiniciar", command=self.reset_selection)
        self.reset_button.pack()

    def add_participant(self):
        participant = self.entry.get()
        if participant:
            self.participants.append(participant)
            messagebox.showinfo("Éxito", f"Participante '{participant}' agregado correctamente.")
            self.entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Por favor, ingrese un nombre de participante.")

    def select_next(self):
        if self.participants:
            if len(self.selected_participants) < len(self.participants):
                remaining_participants = [p for p in self.participants if p not in self.selected_participants]
                selected_participant = random.choice(remaining_participants)
                self.selected_participants.append(selected_participant)
                messagebox.showinfo("Participante Seleccionado", f"El siguiente participante es: {selected_participant}")
            else:
                messagebox.showinfo("Fin", "¡Todos los participantes han sido seleccionados!")
        else:
            messagebox.showerror("Error", "No hay participantes para seleccionar.")

    def reset_selection(self):
        self.selected_participants = []
        messagebox.showinfo("Reinicio", "Selección reiniciada. Puede volver a seleccionar participantes.")

def main():
    root = tk.Tk()
    app = RandomParticipantSelector(root)
    root.mainloop()

if __name__ == "__main__":
    main()
