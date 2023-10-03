import tkinter as tk

root = tk.Tk()
root.geometry('400x400')
root.title('Contador de Cliques')
root.iconbitmap('contador.ico')
root.configure(background='#000')
root.maxsize(400, 400)
root.minsize(400, 400)

numero = 0

def aumentar():
    global numero
    numero = numero + 1
    contagem.configure(text=numero)
    

def diminuir():
    global numero
    numero = numero - 1
    contagem.configure(text=numero)
        

botao = tk.Button(root, bg='#000', text='+', font='gabrila 15', fg='#FFFFFF', padx=8, command=aumentar)
botao.place(x=185, y=120)

contagem = tk.Label(root, bg='#000', text=numero, font='gabriola 20', fg='#FFFFFF')
contagem.place(x=200, y=160)

botao1 = tk.Button(root, bg='#000', text='-', font='gabrila 15', fg='#FFFFFF', padx=10, command=diminuir)
botao1.place(x=185, y=220)



root.mainloop()