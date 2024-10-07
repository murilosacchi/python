import tkinter as tk
from tkinter import messagebox

moedas = ['m25', 'm50', 'm100', 'b']  # entradas
estados = [0, 25, 50, 75, 100, 125, 150, 175, 200]
estado_inicial = 0  # saldo inicial
estado_final = [200]  # preço do refrigerante

# transição de estados
delta = {
    0:{'m25':(25,'n'),'m50':(50,'n'),'m100':(100,'n'),'b':(0,'n')},
    25:{'m25':(50,'n'),'m50':(75,'n'),'m100':(125,'n'),'b':(25,'n')},
    50:{'m25':(75,'n'),'m50':(100,'n'),'m100':(150,'n'),'b':(50,'n')},
    75:{'m25':(100,'n'),'m50':(125,'n'),'m100':(175,'n'),'b':(75,'n')},
    100:{'m25':(125,'n'),'m50':(150,'n'),'m100':(200,'n'),'b':(100,'n')},
    125:{'m25':(150,'n'),'m50':(175,'n'),'m100':(200,'n'),'b':(125,'n')},
    150:{'m25':(175,'n'),'m50':(200,'n'),'m100':(200,'t50'),'b':(150,'n')},
    175:{'m25':(200,'n'),'m50':(200,'t25'),'m100':(200,'t75'),'b':(175,'n')},
    200:{'m25':(200,'t25'),'m50':(200,'t50'),'m100':(200,'t100'),'b':(200,'r')}
}

class MaquinaRefrigerante:
    def __init__(self):
        self.estado = estado_inicial
        self.saldo_total = 0

    def inserir_moeda(self, moeda):
        global delta
        if moeda in delta[self.estado]:
            proximo_estado, troco = delta[self.estado][moeda]
            self.estado = proximo_estado
            
            if moeda.startswith('m'):
                valor = int(moeda[1:])
                self.saldo_total += valor 

            interface.atualizar_saldo(self.saldo_total)
            
        else:
            messagebox.showerror("Erro", "Moeda inválida")

    def liberar_produto(self):
        if self.estado in estado_final:
            troco = (self.saldo_total - 200) / 100
            messagebox.showinfo("Comprou", f"Troco: R${troco:.2f}")
            self.resetar()
        else:
            messagebox.showwarning("Atenção", "Saldo insuficiente para comprar o refrigerante.")

    def resetar(self):
        self.estado = estado_inicial
        self.saldo_total = 0
        interface.atualizar_saldo(self.saldo_total)

# interface grafica
class InterfaceMaquina:
    def __init__(self, root):
        self.root = root
        self.root.title("Máquina de Refrigerante")
        self.root.geometry("250x250")

        self.saldo_label = tk.Label(root, text="Saldo: R$0,00", font=("Arial", 14))
        self.saldo_label.pack(pady=20)

        self.botao_moeda25 = tk.Button(root, text="+ R$0,25", command=lambda: maquina.inserir_moeda('m25'))
        self.botao_moeda25.pack(pady=5)

        self.botao_moeda50 = tk.Button(root, text="+ R$0,50", command=lambda: maquina.inserir_moeda('m50'))
        self.botao_moeda50.pack(pady=5)

        self.botao_moeda100 = tk.Button(root, text="+ R$1,00", command=lambda: maquina.inserir_moeda('m100'))
        self.botao_moeda100.pack(pady=5)

        self.botao_liberar = tk.Button(root, text="Comprar Refrigerante", command=maquina.liberar_produto)
        self.botao_liberar.pack(pady=20)

    def atualizar_saldo(self, saldo):
        self.saldo_label.config(text=f"Saldo: R${saldo/100:.2f}")

maquina = MaquinaRefrigerante()
root = tk.Tk()
interface = InterfaceMaquina(root)
root.mainloop()
