import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

error = True
#Functions
def onClickStartButton():
    print("Botão Iniciar clicado... Executando de no modo ghost.")
    progresso.set(0)
    for _ in range(200):
        progresso.set(progresso.get() + 1) 
        janela.update_idletasks()
        janela.after(10)
    if (error):
        messagebox.showerror("Erro", f'''Erro durante a tentativa de obter os dados. Tente mais uma vez e se caso não funcionar, a conexão pode estar com problemas.''')
    else:
        messagebox.showinfo("Aviso", f'''Processo concluído com sucesso!
O arquivo PDF foi gerado.''')

janela = tk.Tk()
progresso = DoubleVar(janela)
janela.title("Verificador de Buffer")

botao_start = tk.Button(janela, text="Iniciar verificação", command=onClickStartButton, height=3)
botao_start.pack(pady=25, padx=30)

label_barra_progresso = tk.Label(janela, text="Barra de progresso")
label_barra_progresso.pack()

barra_progresso = ttk.Progressbar(janela, variable= progresso, maximum=200, orient="horizontal", length=200, mode="determinate")
barra_progresso.pack(padx=50, pady=10)

janela.mainloop()