# Importación de librerías
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Declaramos variable global
x = 0

# Esta función revisa algo jajaja
def checkQueens(queens, n, k):
    for i in range(0, k):
        if((queens[i] == queens[k]) or (abs(k - i) == abs(queens[k] - queens[i]))):
            return False
    return True

''' Función que resuelve el problema de las N Reinas, recibe 4 parámetros, el array de reinas, el número
de reinas, el contador de incialización, y el diccionario para guardar todas las soluciones, retorna
el número total de soluciones '''
def NQueens(queens, n, k, dictSolutions):
    # Comprueba si k es igual a n
    if(k == n):
        # Definimos a la variable global
        global x
        # Incrementamos el cont
        x = x + 1
        # Definimos el arreglo que guardará soluciones
        sol = []
        # Bucle para iterar al arreglo de reinas
        for i in range(0, n):
            # Al arreglo soluciones le agregamos las reinas
            sol.append(queens[i])
        # Al diccionario le agregamos las soluciones
        dictSolutions[x] = {
            x : sol
        }
    # Si es falso
    else:
        # Iteramos el array de reinas para que verifique si las reinas existen y hace una llamada recursiva a la
        # función NQueens
        for queens[k] in range(0, n):
            if(checkQueens(queens, n, k)):
                NQueens(queens, n, k+1, dictSolutions)
    # Retornamos el total de soluciones
    return x

# Función para la interfaz gráfica y eventos
def window():
    # Definimos root como la ventana
    root = Tk()
    # Damos dimensiones
    root.geometry('1024x600')
    # Título de la ventana
    root.title('N Reinas')

    # Label del título
    mainTitle = ttk.Label(root, text="Problema de las N Reinas")
    mainTitle.pack() 
    mainTitle.config(font=('Arial', 24))
    
    # Espacio jaja
    Label(root, text=" ").pack()

    # Etiqueta label para pedir el número de reinas
    txtEntryQueens = ttk.Label(root, text="Ingrese el número de reinas:")
    txtEntryQueens.pack()
    txtEntryQueens.config(font=('Arial', 16))

    # Etiqueta entry para escribir el número de reinas
    entryQueens = ttk.Entry(root)
    entryQueens.pack()
    entryQueens.config(font=('Arial', 12), justify=("center"))

    # Espacio
    Label(root, text=" ").pack()

    # Estilos para los botones
    s = ttk.Style()
    s.configure(
        "MyButton.TButton",
        font=("Arial", 12),
        background="#000000"
    )

    # Función para obtener y validar el número y mandar a llamar a la función NQueens
    def callQueens():
        k = 0
        dictSolutions = {}
        n = entryQueens.get()
        if n.isdigit():
            m = int(n)
            if(m > 3):
                queens = [-1 for n in range(0, m)]
                numSol = NQueens(queens, m, k, dictSolutions)
                Label(root, text=" ").pack()
                labelSolutions = ttk.Label(root, text=f'Total de soluciones: {numSol}')
                labelSolutions.pack()
                labelSolutions.config(font=('Arial', 16))
                entryQueens['state'] = DISABLED
                btnQueens['state'] = DISABLED

                Label(root, text=" ").pack()
                Label(root, text=" ").pack()

                labelSol = ttk.Label(root, text="Ingrese el número de la solución que desea ver: ")
                labelSol.pack()
                labelSol.config(font=('Arial', 12))
                
                entrySol = ttk.Entry(root)
                entrySol.pack()
                entrySol.config(font=('Arial', 12), justify=("center"))

                def showBoard():
                    print('\nAquí va el código del tablero\n')
                    n = entrySol.get()
                    if n.isdigit():
                        m = int(n)
                        if m > 0 and m <= numSol:
                            print(f'\n{dictSolutions}')
                            ### Aquí va el código del tablero ###
                        else:
                            messagebox.showinfo(f'Entre 0 y {numSol}', f'El número debe ser mayor a 0 y menor a {numSol}.')
                            entrySol.delete("0","end")
                    else:
                        messagebox.showinfo('Sólo números', 'Sólo se permiten números mayores a 0.')
                        entrySol.delete("0","end")

                Label(root, text=" ").pack()

                btnSol = ttk.Button(root, text="Mostrar", style="MyButton.TButton", command=showBoard)
                btnSol.pack()
            else:
                # print("\nEl número debe ser mayor a 3")
                messagebox.showinfo('Mayor a 3', "El número debe ser mayor a 3.")
                entryQueens.delete("0","end")
        else:
            # print('\nSólo se permite ingresar números')
            messagebox.showinfo('Sólo números', 'Sólo se permiten números mayores a 3.')
            entryQueens.delete("0","end")

    btnQueens = ttk.Button(root, text="Enter", style="MyButton.TButton", command=callQueens)
    btnQueens.pack()

    btnExit = ttk.Button(root, text='Salir', command=quit, style="MyButton.TButton")
    btnExit.pack(side=BOTTOM)

    root.mainloop()

window()

'''k = 0
dictSolutions = {}
amount = int(input('\nIngrese la cantidad de reinas: '))

res = NQueens(queens, amount, k, dictSolutions)
print(f'\n\n{res}\n\n')'''