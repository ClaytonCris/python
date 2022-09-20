import tkinter as tk
janela = tk.Tk()
janela.title('Bem vindo python')
texto=tk.Label(janela, text='este e uma label', font=('arial bold', 70))
texto.grid(column=0, row=0)
botao = tk.Button(janela, text='sair', height=5, width = 35, command= janela.destroy)
botao.grid(column=0, row =1)
janela.geometry('1024x768')


janela.mainloop()
