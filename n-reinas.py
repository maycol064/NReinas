# from tkinter import *
# from tkinter import ttk

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
        print("\n")
        dictSolutions[x] = {
            x : sol
        }
    else:
        for queens[k] in range(0, n):
            if(checkQueens(queens, n, k)):
                NQueens(queens, n, k+1, dictSolutions)
    return dictSolutions

# root = Tk()
# root.geometry('800x600')
# root.title('N Reinas')
# mainTitle = Label(root, text="Problema de las N Reinas")
# mainTitle.pack() 
# mainTitle.config(font=('Arial', 24))
# entry = ttk.Entry(root)
# entry.place(x=50, y=50)
# ttk.Button(root, text='Salir', command=quit).pack(side=BOTTOM)
# root.mainloop()

k = 0
dictSolutions = {}
amount = int(input('\nIngrese la cantidad de reinas: '))
queens = [-1 for n in range(0, amount)]
res = NQueens(queens, amount, k, dictSolutions)

print(f'\n\n{res}\n\n')