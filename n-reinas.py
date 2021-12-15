# Importación de librerías
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import *
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import os
import sys

# Declaración de variables globales
x = 0
a = 1

''' Esta función recibe 3 parámetros, las reinas, el número de reinas y k. Y verifica si no son 
iguales los elementos de las reinas'''
def checkQueens(queens, n, k):
    for i in range(0, k):
        if((queens[i] == queens[k]) or (abs(k - i) == abs(queens[k] - queens[i]))):
            return False
    return True

''' Recibe, las reinas, número de reinas, k y el diccionario de soluciones, verifia si k = n, para
agregar el resultado en un array y el array en un diccionario, si no, hace una comprobación de la
función anterior, para hacer una llamada recursiva de esta función. '''
def NQueens(queens, n, k, dictSolutions):
    if(k == n):
        global x
        x = x + 1
        sol = []
        for i in range(0, n):
            sol.append(queens[i])
        dictSolutions[x] = {
            x : sol
        }
    else:
        for queens[k] in range(0, n):
            if(checkQueens(queens, n, k)):
                NQueens(queens, n, k+1, dictSolutions)

''' Función creadora de la interfaz '''
def window():
    # Definimos root como la ventana principal
    root = Tk()
    # Le damos dimensiones
    root.geometry('1024x700')
    # Le asignamos un título
    root.title('N Reinas')
    # Evitamos que se redimensione
    root.resizable(0,0)

    # Widgets que conforman la interfaz
    mainTitle = ttk.Label(root, text="Problema de las N Reinas")
    mainTitle.pack() 
    mainTitle.config(font=('Arial', 18))
    Label(root, text=" ").pack()
    txtEntryQueens = ttk.Label(root, text="Ingrese el número de reinas:")
    txtEntryQueens.pack()
    txtEntryQueens.config(font=('Arial', 12))
    entryQueens = ttk.Entry(root)
    entryQueens.pack()
    entryQueens.config(font=('Arial', 12), justify=("center"))
    # Estilos de los botones
    s = ttk.Style()
    s.configure(
        "MyButton.TButton",
        font=("Arial", 12),
        background="#000000"
    )
    ''' Función para pintar el tablero, usamos matplotlib y un canvas de tkinter, recibe el número de
    soluciones, el diccionario de solcuiones, el número de solución, la figura, el elemento de matplotlib
    y la canva.
    Por cada llamada en la variable array guardamos la solución que guardamos en el diccionario para
    que se pueda acceder a los valores y pintar el tablero '''
    def printBoard(m, dictSolutions, a, fig, ax, canvas):
        # print(f'Solución {a}')
        array = dictSolutions[a][a]
        # Limpiamos el canva y quitamos los ejes
        ax.clear()
        ax.axis('off')
        # Ciclo para iterar y dibujar el tablero
        for i in range(0, m+1):
            ax.plot([0, m], [i, i], color="gray")
            ax.plot([i, i], [m, 0], color="gray")
        # Ciclo para colocar la reina
        for i in range(0, m):
            if array[i] != -1:
                ax.plot([i+0.5], [array[i]+0.5], marker=".", markersize=30, color="black")
        plt.tight_layout()
        ax.patch.set_visible(False)
        # Dibujar canva
        canvas.draw()
        canvas.get_tk_widget().pack()
        a += 1

    # Función que agregar más widgets a la interfaz y comprueba si el número ingresado fue correcto
    def callQueens():
        k = 0
        global a
        dictSolutions = {}
        n = entryQueens.get()
        if n.isdigit():
            m = int(n)
            if(m > 3 and m < 11):
                queens = [-1 for n in range(0, m)]
                numSol = NQueens(queens, m, k, dictSolutions)
                entryQueens['state'] = DISABLED
                btnQueens['state'] = DISABLED
                Label(root, text=" ").pack()
                labelSolutions = ttk.Label(root, text=f'Total de soluciones: {x}')
                labelSolutions.pack()
                labelSolutions.config(font=('Arial', 12))
                view = ttk.Label(root, text="Ingrese el número de la solución que desea ver:")
                view.pack()
                view.config(font=('Arial', 12))
                txtView = ttk.Entry(root)
                txtView.pack()
                txtView.config(font=('Arial', 12), justify=("center"))
                # Verficia si el número es correcto para pintar más widgets y mandar a llamar la función del tablero
                def verify(m, dictSolutions):
                    a = txtView.get()
                    if a.isdigit():
                        b = int(a)
                        if(b > 0 and b <= x):
                            txtRes = ttk.Label(root, text=f'Solución{a}')
                            txtRes.config(font=('Arial', 12))
                            txtRes.pack()
                            printBoard(m, dictSolutions, b, fig, ax, canvas)
                            txtView.delete("0","end")
                        else:
                            # Mensajes de error
                            messagebox.showinfo(f'Mayor a 0', f'El número debe ser mayor 0 y menor a {x+1}')
                            txtView.delete("0","end")
                    else:
                        # Mensajes de error
                        messagebox.showinfo('Sólo números', 'Sólo se permiten números.')
                        txtView.delete("0","end")
                # Declaración del canvas
                fig = Figure(frameon=False)
                ax = fig.add_subplot(111)
                canvas = FigureCanvasTkAgg(fig, root)
                btnView = ttk.Button(root, text="Ver", style="MyButton.TButton", command=lambda:verify(m ,dictSolutions))
                btnView.pack()
            else:
                # Mensajes de error
                messagebox.showinfo('Mayor a 3', "El número debe ser mayor a 3 y menor a 11")
                entryQueens.delete("0","end")
        else:
            # Mensajes de error
            messagebox.showinfo('Sólo números', 'Sólo se permiten números mayores a 3.')
            entryQueens.delete("0","end")
    btnQueens = ttk.Button(root, text="Generar", style="MyButton.TButton", command=callQueens)
    btnQueens.pack()
    # Reincia la ventana para poder ingresar más datos
    def restart():
        os.execl(sys.executable, sys.executable, * sys.argv)
    btnExit = ttk.Button(root, text='Limpiar', command=restart, style="MyButton.TButton")
    btnExit.pack(side=BOTTOM)
    # Convierte a root en la ventana principal
    root.mainloop()
# Llamada de la interfaz
window()