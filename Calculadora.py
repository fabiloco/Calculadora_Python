from tkinter import *
from tkinter import font as font


operacion=""
resultado=0

root=Tk()
root.iconbitmap("calcIcon.ico")
root.title("Calculadora")
root.resizable(0,0)

frame=Frame(root, bg="cyan")


frame.pack()

#*** The font object***

myFont=font.Font(family='Times New Roman', size=20, weight='bold')
myFont2=font.Font(family='Times New Roman', size=20)

#***EXTRAS***

numeroPantalla=StringVar()

tf1=Entry(frame, font=myFont2, textvariable=numeroPantalla)
tf1.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

#***BOTONES***

#PRIMERA FILA

boton1=Button(frame,text="1", font=myFont, padx=16, pady=10, command=lambda:self.AddVal("1"))
boton1.grid(row=1, column=0, padx=3, pady=3)

boton2=Button(frame, text="2", font=myFont, padx=16, pady=10, command=lambda:self.AddVal("2"))
boton2.grid(row=1, column=1, padx=3, pady=3)

boton3=Button(frame, text="3", font=myFont, padx=16, pady=10, command=lambda:self.AddVal("3"))
boton3.grid(row=1, column=2, padx=3, pady=3)

    #BOTON SUMAR
botonSumar=Button(frame, text="+", font=myFont, padx=16, pady=10, command=lambda:self.Suma(numeroPantalla.get()))
botonSumar.grid(row=1, column=3, padx=3, pady=3)

#SEGUNDA FILA

boton4=Button(frame, text="4", font=myFont, padx=16, pady=10, command=lambda:self.AddVal("4"))
boton4.grid(row=2, column=0, padx=3, pady=3)

boton5=Button(frame, text="5", font=myFont, padx=16, pady=10, command=lambda:self.AddVal("5"))
boton5.grid(row=2, column=1, padx=3, pady=3)

boton6=Button(frame, text="6", font=myFont, padx=16, pady=10, command=lambda:self.AddVal("6"))
boton6.grid(row=2, column=2, padx=3, pady=3)

    #BOTON RESTAR
botonRestar=Button(frame, text="-", font=myFont, padx=18, pady=10)
botonRestar.grid(row=2, column=3, padx=3, pady=3)

#TERCERA FILA

boton7=Button(frame, text="7", font=myFont, padx=16, pady=10, command=lambda:self.AddVal("7"))
boton7.grid(row=3, column=0, padx=3, pady=3)

boton8=Button(frame, text="8", font=myFont, padx=16, pady=10, command=lambda:self.AddVal("8"))
boton8.grid(row=3, column=1, padx=3, pady=3)

boton9=Button(frame, text="9", font=myFont, padx=16, pady=10, command=lambda:self.AddVal("9"))
boton9.grid(row=3, column=2, padx=3, pady=3)

    #BOTON DIVIDIR
botonDividir=Button(frame, text="÷", font=myFont, padx=16, pady=10)
botonDividir.grid(row=3, column=3, padx=3, pady=3)

#CUARTA FILA

boton0=Button(frame, text="0", font=myFont, padx=16, pady=10, command=lambda:self.AddVal("0"))
boton0.grid(row=4, column=0, padx=3, pady=3)

botonPunto=Button(frame, text=",", font=myFont, padx=19, pady=10, command=lambda:self.AddVal(","))
botonPunto.grid(row=4, column=1, padx=3, pady=3)

botonMultiplicar=Button(frame, text="*", font=myFont, padx=16, pady=10)
botonMultiplicar.grid(row=4, column=2, padx=3, pady=3)

botonIgual=Button(frame, text="=", font=myFont, padx=16, pady=48, command = lambda:self.igual(resultado))
botonIgual.grid(row=4, column=3, rowspan=5, padx=3, pady=3)

#QUINTA FILA

botonBorrarTodo=Button(frame, text="MC", font=myFont, padx=38, pady=10)
botonBorrarTodo.grid(row=5, column=0, columnspan=2, padx=3, pady=3)

botonBorrar=Button(frame, text="<", font=myFont, padx=16, pady=10)
botonBorrar.grid(row=5, column=2, padx=3, pady=3)

#***FIN BOTONES***

def AddVal(self, num):
    #print(operacion)
    if operacion != "":
        numeroPantalla.set(num)
        operacion = ""
    else:
        numeroPantalla.set(numeroPantalla.get() + num)


def Suma(self, num):

    resultado+=int(num)

    operacion="suma"

    numeroPantalla.set(resultado)


def igual(self, resultado):

    numeroPantalla.set(resultado + int(numeroPantalla.get()))

    resultado = 0
