import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        self.entrada = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right')
        self.entrada.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

        self.criar_botoes()

    def adicionar_valor(self, valor):
        atual = self.entrada.get()
        self.entrada.delete(0, tk.END)
        self.entrada.insert(0, atual + str(valor))

    def calcular(self):
        try:
            resultado = eval(self.entrada.get())
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, str(resultado))
        except:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, "Erro")

    def limpar(self):
        self.entrada.delete(0, tk.END)

    def criar_botoes(self):
        botoes = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for linha in botoes:
            frame = tk.Frame(self.root)
            frame.pack(expand=True, fill='both')
            for btn in linha:
                if btn == '=':
                    comando = self.calcular
                else:
                    comando = lambda b=btn: self.adicionar_valor(b)
                botao = tk.Button(frame, text=btn, font=("Arial", 18), relief=tk.GROOVE, command=comando)
                botao.pack(side=tk.LEFT, expand=True, fill='both')

        frame_clear = tk.Frame(self.root)
        frame_clear.pack(expand=True, fill='both')
        btn_clear = tk.Button(frame_clear, text='C', font=("Arial", 18), bg='red', fg='white',
                              command=self.limpar)
        btn_clear.pack(side=tk.LEFT, expand=True, fill='both')

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()