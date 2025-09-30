from tkinter import Button
import random
import ajustes


class Celda:
    todas = []
    def __init__(self, x, y, es_mina=False):
        self.es_mina = es_mina
        self.objeto_boton_celda = None
        self.x = x
        self.y = y

        # Agregar el objeto a la lista Celda.todas
        Celda.todas.append(self)

    def crear_objeto_boton(self, ubicacion):
        boton = Button(
            ubicacion,
            width=12,
            height=4,
            text=f"{self.x},{self.y}"
        )
        boton.bind('<Button-1>', self.acciones_click_izquierdo)  # Clic Izquierdo
        boton.bind('<Button-3>', self.acciones_click_derecho)    # Clic Derecho
        self.objeto_boton_celda = boton

    def acciones_click_izquierdo(self, evento):
        print(evento)
        print("¡Me hicieron clic izquierdo!")

    def acciones_click_derecho(self, evento):
        print(evento)
        print("¡Me hicieron clic derecho!")

    @staticmethod
    def aleatorizar_minas():
        celdas_seleccionadas = random.sample(
            Celda.todas, ajustes.CANTIDAD_MINAS
        )
        for celda in celdas_seleccionadas:
            celda.es_mina = True

    def __repr__(self):
        return f"Celda({self.x}, {self.y})"
