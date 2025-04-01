import tkinter as tk
from tkinter import messagebox

def validar_senha():
    senha = entrada_senha.get()
    tem_oito_caracteres = len(senha) >= 8
    tem_numero = any(c.isdigit() for c in senha)

    # Implemente o conectivo lógico "AND" para verificar se ambas as condições são verdadeiras
    # Preencha a linha abaixo com o conectivo apropriado
    if :
        messagebox.showinfo("Sucesso", "Senha válida!")
    else:
        messagebox.showerror("Erro", "Senha inválida. Deve ter pelo menos 8 caracteres e conter pelo menos um número.")

# Cria a janela principal
janela = tk.Tk()
janela.title("Validador de Senha")

# Cria os widgets
label_senha = tk.Label(janela, text="Digite a senha:")
entrada_senha = tk.Entry(janela, show="*")  # Oculta a senha
botao_validar = tk.Button(janela, text="Validar", command=validar_senha)

# Posiciona os widgets na janela
label_senha.pack()
entrada_senha.pack()
botao_validar.pack()

# Inicia o loop principal da interface
janela.mainloop()
