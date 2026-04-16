import tkinter as tk

lista_nomes = []

def AdicionarNome(entrada, label):
    novo_nome = entrada.get().strip()
    entrada.delete(0, tk.END)
    if novo_nome:
        lista_nomes.append(novo_nome)
        texto_exibicao = "\n".join(lista_nomes)
        label.config(text=f"Lista: \n{texto_exibicao}")

def Main():
    
    app = tk.Tk()
    app.title("")
    app.geometry("370x400")

    #Instrução
    information = tk.Label(app, text="Gerenciador de Nomes")
    information.pack(pady=(20, 5))

    #Campo de entrada
    entrada_nome = tk.Entry(app, width=30)
    entrada_nome.pack(pady=5)

    #Botão para adcionar nome a lista
    button = tk.Button(app, text="Adicionar", command=lambda:AdicionarNome(entrada_nome, label_lista))
    button.pack()

    # Label onde a lista aparece 
    label_lista = tk.Label(app, text="Lista: \n")
    label_lista.pack(pady=10)

    app.mainloop()
    
if __name__ == "__main__":
    Main()