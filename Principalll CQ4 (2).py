from tkinter import *
from celda import Celda
import ajustes
import utilidades


ventana = Tk()
# Configuración de la ventana
ventana.configure(bg="black")
ventana.geometry(f'{ajustes.ANCHO}x{ajustes.ALTO}')
ventana.title("Juego Buscaminas")
ventana.resizable(False, False)

marco_superior = Frame(
    ventana,
    bg='black',
    width=ajustes.ANCHO,
    height=utilidades.alto_prct(25)
)
marco_superior.place(x=0, y=0)

marco_izquierdo = Frame(
    ventana,
    bg='black',
    width=utilidades.ancho_prct(25),
    height=utilidades.alto_prct(75)
)
marco_izquierdo.place(x=0, y=utilidades.alto_prct(25))

marco_central = Frame(
    ventana,
    bg='black',
    width=utilidades.ancho_prct(75),
    height=utilidades.alto_prct(75)
)
marco_central.place(
    x=utilidades.ancho_prct(25),
    y=utilidades.alto_prct(25),
)

for x in range(ajustes.TAMANO_CUADRICULA):
    for y in range(ajustes.TAMANO_CUADRICULA):
        celda = Celda(x, y)
        celda.crear_objeto_boton(marco_central)
        celda.objeto_boton_celda.grid(
            column=x, row=y
        )

Celda.aleatorizar_minas()

# Ejecutar la ventana
ventana.mainloop()
