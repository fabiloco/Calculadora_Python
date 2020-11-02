from tkinter import *
from tkinter import font as font

class Interfaz:

    def __init__(self):
        self._root=Tk()
        self._root.iconbitmap("calcIcon.ico")
        self._root.title("Calculadora")
        self._frame=Frame(self._root, bg="cyan")

        self._frame.pack()

        #*** The font object***

        self._myFont=font.Font(family='Times New Roman', size=20, weight='bold')
        self._myFont2=font.Font(family='Times New Roman', size=20)
        #***BOTONES***

        #PRIMERA FILA

        self._boton1=Button(self._frame,text="1", font=self._myFont, padx=16, pady=10)
        self._boton1.grid(row=1, column=0, padx=3, pady=3)

        self._boton2=Button(self._frame, text="2", font=self._myFont, padx=16, pady=10)
        self._boton2.grid(row=1, column=1, padx=3, pady=3)

        self._boton3=Button(self._frame, text="3", font=self._myFont, padx=16, pady=10)
        self._boton3.grid(row=1, column=2, padx=3, pady=3)

            #BOTON SUMAR
        self._botonSumar=Button(self._frame, text="+", font=self._myFont, padx=16, pady=10)
        self._botonSumar.grid(row=1, column=3, padx=3, pady=3)

        #SEGUNDA FILA

        self._boton4=Button(self._frame, text="4", font=self._myFont, padx=16, pady=10)
        self._boton4.grid(row=2, column=0, padx=3, pady=3)

        self._boton5=Button(self._frame, text="5", font=self._myFont, padx=16, pady=10)
        self._boton5.grid(row=2, column=1, padx=3, pady=3)

        self._boton6=Button(self._frame, text="6", font=self._myFont, padx=16, pady=10)
        self._boton6.grid(row=2, column=2, padx=3, pady=3)

            #BOTON RESTAR
        self._botonRestar=Button(self._frame, text="-", font=self._myFont, padx=18, pady=10)
        self._botonRestar.grid(row=2, column=3, padx=3, pady=3)

        #TERCERA FILA

        self._boton7=Button(self._frame, text="7", font=self._myFont, padx=16, pady=10)
        self._boton7.grid(row=3, column=0, padx=3, pady=3)

        self._boton8=Button(self._frame, text="8", font=self._myFont, padx=16, pady=10)
        self._boton8.grid(row=3, column=1, padx=3, pady=3)

        self._boton9=Button(self._frame, text="9", font=self._myFont, padx=16, pady=10)
        self._boton9.grid(row=3, column=2, padx=3, pady=3)

            #BOTON DIVIDIR
        self._botonDividir=Button(self._frame, text="÷", font=self._myFont, padx=16, pady=10)
        self._botonDividir.grid(row=3, column=3, padx=3, pady=3)

        #CUARTA FILA

        self._boton0=Button(self._frame, text="0", font=self._myFont, padx=16, pady=10)
        self._boton0.grid(row=4, column=0, padx=3, pady=3)

        self._botonPunto=Button(self._frame, text=".", font=self._myFont, padx=19, pady=10)
        self._botonPunto.grid(row=4, column=1, padx=3, pady=3)

        self._botonMultiplicar=Button(self._frame, text="*", font=self._myFont, padx=16, pady=10)
        self._botonMultiplicar.grid(row=4, column=2, padx=3, pady=3)

        self._botonIgual=Button(self._frame, text="=", font=self._myFont, padx=16, pady=48)
        self._botonIgual.grid(row=4, column=3, rowspan=5, padx=3, pady=3)

        #QUINTA FILA

        self._botonBorrarTodo=Button(self._frame, text="MC", font=self._myFont, padx=38, pady=10)
        self._botonBorrarTodo.grid(row=5, column=0, columnspan=2, padx=3, pady=3)

        self._botonBorrar=Button(self._frame, text="<", font=self._myFont, padx=16, pady=10)
        self._botonBorrar.grid(row=5, column=2, padx=3, pady=3)

        #***FIN BOTONES***

        #***EXTRAS***

        self._tf1=Entry(self._frame, font=self._myFont2)
        self._tf1.grid(row=0, column=0, columnspan=4, padx=5, pady=5)


        self._root.mainloop()


if __name__ == '__main__':

    calculadora=Interfaz()
