import tkinter as tk
from tkinter import ttk

def formulario():
    nomeproduto = entry_nomeproduto.get()
    descricaoproduto = entry_descricaoproduto.get()
    valorproduto = entry_valorproduto.get()
    disponivelvenda = var_disponivelvenda.get()

    print("Nome do produto:", nomeproduto)
    print("Descrição do produto:", descricaoproduto)
    print("Valor do produto:", valorproduto)
    print("Disponível para venda:", disponivelvenda)


root = tk.Tk()
root.title("Cadastro de Produto")


nomeproduto_label = tk.Label(root, text="Nome do Produto:")
nomeproduto_label.grid(row=0, column=0, padx=10, pady=5)
entry_nomeproduto = tk.Entry(root)
entry_nomeproduto.grid(row=0, column=1, padx=10, pady=5)


descricaoproduto_label = tk.Label(root, text="Descrição do Produto:")
descricaoproduto_label.grid(row=1, column=0, padx=10, pady=5)
entry_descricaoproduto = tk.Entry(root)
entry_descricaoproduto.grid(row=1, column=1, padx=10, pady=5)


valorproduto_label = tk.Label(root, text="Valor do Produto:")
valorproduto_label.grid(row=2, column=0, padx=10, pady=5)
entry_valorproduto = tk.Entry(root)
entry_valorproduto.grid(row=2, column=1, padx=10, pady=5)


disponivelvenda_label = tk.Label(root, text="Disponível para Venda:")
disponivelvenda_label.grid(row=3, column=0, padx=10, pady=5)
var_disponivelvenda = tk.StringVar(root)
var_disponivelvenda.set("Sim")


botao_menu = tk.OptionMenu(root, var_disponivelvenda, "Sim", "Não")
botao_menu.grid(row=3, column=1, padx=10, pady=5)
botaosubmeter = tk.Button(root, text="Enviar", command=formulario)
botaosubmeter.grid(row=4, column=0, columnspan=2, padx=10, pady=5)


root.mainloop()