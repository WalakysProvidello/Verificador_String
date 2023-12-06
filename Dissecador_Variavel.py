import tkinter as tk
import re

def verificar():
    valor = entry.get()
    resultado.delete(1.0, tk.END)  # Limpa a área de texto antes de exibir novos resultados

    resultado.insert(tk.END, "O tipo primitivo desse valor é " + str(type(valor)) + "\n")
    resultado.insert(tk.END, "Só tem espaços? " + str(valor.isspace()) + "\n")
    resultado.insert(tk.END, "É um número? " + str(valor.isnumeric()) + "\n")
    resultado.insert(tk.END, "É alfabético? " + str(valor.isalpha()) + "\n")
    resultado.insert(tk.END, "É alfanumérico? " + str(valor.isalnum()) + "\n")
    resultado.insert(tk.END, "Está em maiúsculas? " + str(valor.isupper()) + "\n")
    resultado.insert(tk.END, "Está em minúsculas? " + str(valor.islower()) + "\n")
    resultado.insert(tk.END, "Está capitalizada? " + str(valor.istitle()) + "\n")

def remover_especiais():
    valor = entry.get()
    valor_sem_especiais = re.sub(r'[^A-Za-z0-9 ]+', '', valor)
    resultado.delete(1.0, tk.END)
    resultado.insert(tk.END, "Texto sem caracteres especiais: " + valor_sem_especiais + "\n")

def contar_palavras():
    valor = entry.get()
    palavras = valor.split()
    resultado.delete(1.0, tk.END)

    if len(palavras) > 100:
        resultado.insert(tk.END, "O texto tem mais de 100 palavras. Limite excedido.\n")
    else:
        resultado.insert(tk.END, "Quantidade de palavras: " + str(len(palavras)) + "\n")

# Criar a janela principal
root = tk.Tk()
root.title("Verificador de Strings")
root.geometry("600x600")

# Adicionar entrada de texto
entry_label = tk.Label(root, text="Digite algo:")
entry_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
entry = tk.Entry(root, width=50)
entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

# Adicionar botões
verificar_button = tk.Button(root, text="Verificar", command=verificar)
verificar_button.grid(row=1, column=0, columnspan=2, pady=10)

remover_especiais_button = tk.Button(root, text="Remover Caracteres Especiais", command=remover_especiais)
remover_especiais_button.grid(row=2, column=0, columnspan=2, pady=10)

contar_palavras_button = tk.Button(root, text="Contar Palavras (limite 100)", command=contar_palavras)
contar_palavras_button.grid(row=3, column=0, columnspan=2, pady=10)

# Adicionar área de texto para exibir resultados
resultado_label = tk.Label(root, text="Resultados:")
resultado_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
resultado = tk.Text(root, height=20, width=70)
resultado.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Iniciar o loop principal da interface gráfica
root.mainloop()
