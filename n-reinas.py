from tkinter import *
from tkinter import ttk
from tkinter import messagebox

x = 0

def checkQueens(queens, n, k):
    for i in range(0, k):
        if((queens[i] == queens[k]) or (abs(k - i) == abs(queens[k] - queens[i]))):
            return False
    return True

def NQueens(queens, n, k, dictSolutions):
    if(k == n):
        global x
        x = x + 1
        sol = []
        # print(f'Solución: {x}: ', end="")
        for i in range(0, n):
            # print(f'{queens[i]} , ', end="")
            sol.append(queens[i])
        # print("\n")
        dictSolutions[x] = {
            x : sol
        }
    else:
        for queens[k] in range(0, n):
            if(checkQueens(queens, n, k)):
                NQueens(queens, n, k+1, dictSolutions)
    return x

def window():
    root = Tk()
    root.geometry('1024x600')
    root.title('N Reinas')

    mainTitle = ttk.Label(root, text="Problema de las N Reinas")
    mainTitle.pack() 
    mainTitle.config(font=('Arial', 24))
    
    Label(root, text=" ").pack()

    txtEntryQueens = ttk.Label(root, text="Ingrese el número de reinas:")
    txtEntryQueens.pack()
    txtEntryQueens.config(font=('Arial', 16))

    entryQueens = ttk.Entry(root)
    entryQueens.pack()
    entryQueens.config(font=('Arial', 12), justify=("center"))

    Label(root, text=" ").pack()

    def callQueens():
        k = 0
        dictSolutions = {}
        n = entryQueens.get()
        if n.isdigit():
            m = int(n)
            if(m > 3):
                queens = [-1 for n in range(0, m)]
                res = NQueens(queens, m, k, dictSolutions)
                # print(f'\n{res}')
                # print(f'\n{dictSolutions}')
                Label(root, text=" ").pack()
                labelSolutions = ttk.Label(root, text=f'Total de soluciones: {res}')
                labelSolutions.pack()
                labelSolutions.config(font=('Arial', 16))
                entryQueens['state'] = DISABLED
                btnQueens['state'] = DISABLED

                ### AQUÍ SE SUPONE QUE VA EL CÓDIGO PA LA GRÁFICA ###

                Label(root, text=" ").pack()
                Label(root, text=" ").pack()
                Label(root, text=" ").pack()

                labelSol = ttk.Label(root, text="Ingrese el número de la solución que desea ver: ")
                labelSol.pack()
                labelSol.config(font=('Arial', 12))
            else:
                # print("\nEl número debe ser mayor a 3")
                messagebox.showinfo('Mayor a 3', "El número debe ser mayor a 3.")
                entryQueens.delete("0","end")
        else:
            # print('\nSólo se permite ingresar números')
            messagebox.showinfo('Sólo números', 'Sólo se permiten números mayores a 3.')
            entryQueens.delete("0","end")

    s = ttk.Style()
    s.configure(
        "MyButton.TButton",
        font=("Arial", 12),
        background="#000000"
    )

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