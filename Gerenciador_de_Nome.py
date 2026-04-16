import tkinter as tk

lista_nomes = []

def AdicionarNome(entrada, listbox):
    novo_nome = entrada.get().strip()
    if novo_nome:

        listbox.insert(tk.END, novo_nome)
        entrada.delete(0, tk.END)

def removeSelecionado(listbox):
    selecao = listbox.curselection()
    if selecao:
        listbox.delete(selecao)

def LimparLista(listbox):
    listbox.delete(0, tk.END)

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
    buttonAdd = tk.Button(app, text="Adicionar", command=lambda:AdicionarNome(entrada_nome, listbox))
    buttonAdd.pack(pady=10)

    buttonRemove = tk.Button(app, text="Remover", command=lambda:removeSelecionado(listbox))
    buttonRemove.pack()


    buttonClean = tk.Button(app, text="Limpar Lista", command=lambda:LimparLista(listbox))
    buttonClean.pack(pady=10)


    # Box onde a lista aparece 
    # label_lista = tk.Label(app, text="Lista: \n")
    listbox = tk.Listbox(app, width=30, height=10)
    listbox.pack(pady=5)

    #Adicionar tembem ao selecionar 'Enter'
    app.bind('<Return>', lambda event: AdicionarNome(entrada_nome, listbox))

    app.mainloop()
    
if __name__ == "__main__":
    Main()