#importação de bibliotecas e arquivos.
import customtkinter as ctk
from tkinter import *
from Menu_Papel import *
from Menu_Papelao import *
from Menu_Plastico import *
from Menu_Vidro import *
from Menu_Descarte import *

def atual_pagina(pagina): #Função para mostrar a pagina desejada.
    for frame in frames:
        frame.pack_forget()  #Esconde todas as páginas
    frames[pagina].pack(fill="both", expand=True)  #Mostra a página desejada

#Menu inicial onde terão as opções dos materias que o usuario queira reciclar.
def pag_menu():
    pagina_menu = ctk.CTkFrame(janela) #Cria uma pagina dentro da janela.
    pagina_menu._set_appearance_mode("dark") #Muda o tema para escuro.
    label1 = ctk.CTkLabel(pagina_menu, text="Menu inicial", font=("Arial", 24)) #Adiciona a frase principal da página e muda a fonte dela.
    label1._set_appearance_mode("dark") #Muda o tema para escuro.
    label1.pack(pady=50) #ajusta a distancia vertical para 50 (de cima para baixo).

    botao_papel = ctk.CTkButton(pagina_menu, text="Papel", command=lambda: atual_pagina(1), fg_color="white", text_color="black", hover_color="grey")
    botao_papel._set_appearance_mode("dark")
    botao_papel.pack(pady=20)

    botao_papelao = ctk.CTkButton(pagina_menu, text="Papelão", command=lambda: atual_pagina(5), fg_color="#8B4513", hover_color="#654321")
    botao_papelao._set_appearance_mode("dark")
    botao_papelao.pack(pady=20)

    botao_plastico = ctk.CTkButton(pagina_menu, text="Plástico", command=lambda: atual_pagina(8), fg_color="#A7C7E7", text_color="black", hover_color="#B0E0E6")
    botao_plastico._set_appearance_mode("dark")
    botao_plastico.pack(pady=20)

    botao_vidro = ctk.CTkButton(pagina_menu, text="Vidro", command=lambda: atual_pagina(11), fg_color="#CED4DA", hover_color="#6C757D", text_color="black")
    botao_vidro._set_appearance_mode("dark")
    botao_vidro.pack(pady=20)

    botao_descarte = ctk.CTkButton(pagina_menu, text="Descarte", command=lambda: atual_pagina(12))
    botao_descarte._set_appearance_mode("dark")
    botao_descarte.pack(pady=20)

    return pagina_menu

janela = ctk.CTk() #Cria a Janela Principal que ira rodar o programa.
janela.geometry("800x500")
janela._set_appearance_mode("dark")

#atribuição de páginas à variáveis.
menu = lambda: atual_pagina(0)

rolo = lambda: atual_pagina(2)
papel = lambda: atual_pagina(3)
jornal = lambda: atual_pagina(4)

papelao = lambda: atual_pagina(6)
caixa = lambda: atual_pagina(7)

plastico = lambda: atual_pagina(9)
tampa = lambda: atual_pagina(10)

#Páginas do Programa
frames = [
    pag_menu(),                                                  #Menu
    pag_papel(janela, menu, rolo, papel, jornal),                #Inicio da parte do Papel.
    pag_rolo_papel(janela, menu, lambda: atual_pagina(1)),
    pag_papel_escolha(janela, menu, lambda: atual_pagina(1)),
    pag_papel_jornal(janela, menu, lambda: atual_pagina(1)),
    pag_papelao(janela, menu, papelao, caixa),                   #Inicio da parte do Papelão.
    pag_papelao_escolha(janela, menu, lambda: atual_pagina(5)),
    pag_caixa(janela, menu, lambda: atual_pagina(5)),
    pag_plastico(janela, menu, plastico, tampa),                 #Inicio da parte do Plástico.
    pag_plastico_escolha(janela, menu, lambda: atual_pagina(8)),
    pag_tampa(janela, menu, lambda: atual_pagina(8)),
    pag_vidro(janela, menu),                                     #Inicio da parte do Vidro.
    pag_descarte(janela, menu)                                   #Inicio da parte do Descarte.
]
                                                                 #Fim do Menu

atual_pagina(0) #Inicia o programa no menu inicial.

janela.mainloop()