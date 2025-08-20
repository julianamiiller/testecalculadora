import tkinter as tk

def clicar_botao(valor):
    entrada.insert(tk.END, valor)

def limpar():
    entrada.delete(0, tk.END)

def calcular(event=None): 
    try:
        expressao = entrada.get()
        resultado = eval(expressao)
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

# Janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("320x430")
janela.configure(bg="#1e1e1e")

# Campo de entrada
entrada = tk.Entry(janela, font=("Arial", 24), bg="#2d2d2d", fg="white", borderwidth=2, relief="flat", justify="right")
entrada.pack(padx=10, pady=20, fill="both")
entrada.focus_set()

# Teclas do teclado
janela.bind('<Return>', calcular)

# Estilo dos botões
def criar_botao(frame, texto, cor="#3a3a3a", cor_texto="white", comando=None):
    return tk.Button(frame, text=texto, font=("Arial", 18), bg=cor, fg=cor_texto,
                     relief="flat", command=comando).pack(side="left", expand=True, fill="both", padx=1, pady=1)

# Botões
botoes = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for linha in botoes:
    frame = tk.Frame(janela, bg="#1e1e1e")
    frame.pack(expand=True, fill="both")
    for botao in linha:
        if botao == '=':
            comando = calcular
            cor = "#4caf50"
        else:
            comando = lambda valor=botao: clicar_botao(valor)
            cor = "#3a3a3a"
        criar_botao(frame, botao, cor, comando=comando)

# Botão limpar
frame_clear = tk.Frame(janela, bg="#1e1e1e")
frame_clear.pack(expand=True, fill="both")
criar_botao(frame_clear, "C", cor="#e53935", comando=limpar)

new_var = janela.mainloop()