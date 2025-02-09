import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
from receitas_vidro import *

def descarte_lista(pag_atual, descarte):
    pag_atual.pack_forget()
    descarte()

def voltar_func(atual, anterior): #Função para voltar a pagina anterior dentro nas paginas temporarias do def
    atual.pack_forget()
    anterior.pack(fill="both", expand=True)

def menu_func(atual, menu): #Função para voltar ao menu dentro nas paginas temporarias do def
    atual.pack_forget()
    botao_menu_final = ctk.CTkButton(atual, text="Menu", command=menu())

def apagar(label): #Função para apagar uma label
    label.destroy()

def pag_menu_vidro(janela, menu, garrafas_vidro): # Função do menu do vidro.

    pagina_menu_vidro = ctk.CTkFrame(janela) # Cria a página do menu do vidro.
    pagina_menu_vidro._set_appearance_mode("dark")

    label2 = ctk.CTkLabel(pagina_menu_vidro, text="Escolha", font=("Arial", 24)) # Cria o texto do menu do vidro: "Escolha".
    label2._set_appearance_mode("dark")
    label2.pack(pady=50)

    botao_garrafas_vidro = ctk.CTkButton(pagina_menu_vidro, text="Garrafa de Vidro", command=garrafas_vidro, fg_color="#CED4DA", hover_color="#6C757D", text_color="black") # Botão para avançar para a pagina da Garrafa de Vidro.
    botao_garrafas_vidro._set_appearance_mode("dark")
    botao_garrafas_vidro.pack(pady=20)

    botao_vidro_menu = ctk.CTkButton(pagina_menu_vidro, text="Menu", font=("Arial", 24), width=100, height=40, command=menu) # Botão para voltar ao menu.
    botao_vidro_menu._set_appearance_mode("dark")
    botao_vidro_menu.pack(side="bottom", pady=20)

    return pagina_menu_vidro

def pag_vidro(janela, menu, voltar, descarte): # Função da página do vidro.

    pagina_vidro = ctk.CTkFrame(janela) # Cria a página do vidro.
    pagina_vidro._set_appearance_mode("dark")

    def nao_menor():

        pagina_vidro.pack_forget() # "Esquece" ou fecha a página anterior.

        pagina_receita_maior = ctk.CTkFrame(janela)
        pagina_receita_maior._set_appearance_mode("dark")
        pagina_receita_maior.pack(fill="both", expand=True)

        label_receitas = ctk.CTkLabel(pagina_receita_maior, text="Receita caso a garrafa tenha uma capacidade maior que 500 ml", font=("Arial", 24))
        label_receitas._set_appearance_mode("dark")
        label_receitas.pack(pady=50)

        botao_receita_maior(pagina_receita_maior, janela, menu, menu_func, voltar_func).pack(pady=10)

        botao_descarte = ctk.CTkButton(pagina_receita_maior, text="Descarte",
                                       # botao para ir a pagina de descarte caso o usuario nao queira fazer as receitas.
                                       command=lambda: descarte_lista(pagina_receita_maior, descarte))
        botao_descarte._set_appearance_mode("dark")
        botao_descarte.pack(pady=10)

        label_espaco = ctk.CTkLabel(pagina_receita_maior, text="")  # Label que cria um espaço na página.
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(side="bottom", pady=0)

        botao_fim = ctk.CTkButton(pagina_receita_maior, text="Fim", font=("Arial", 24), width=100,
                                  # Botão que avança para a página final.
                                  height=40, fg_color="Red", text_color="White",
                                  command=lambda: fim_receita(pagina_receita_maior, janela, menu, menu_func, voltar_func))
        botao_fim._set_appearance_mode("dark")
        botao_fim.pack(side="bottom", pady=5)

        botao_result_jornal_menu = ctk.CTkButton(pagina_receita_maior, text="Menu", font=("Arial", 24), width=100,
                                                 # botao para voltar ao menu inicial dentro da pagina temporaria.
                                                 height=40,
                                                 command=lambda: menu_func(pagina_receita_maior, menu))
        botao_result_jornal_menu._set_appearance_mode("dark")
        botao_result_jornal_menu.pack(side="bottom", pady=5)

        botao_result_jornal_voltar = ctk.CTkButton(pagina_receita_maior, text="Voltar", font=("Arial", 24),
                                                   # botao para voltar a pagina anterior dentro da pagina temporaria.
                                                   width=100, height=40,
                                                   command=lambda: voltar_func(pagina_receita_maior, pagina_vidro))
        botao_result_jornal_voltar._set_appearance_mode("dark")
        botao_result_jornal_voltar.pack(side="bottom", pady=5)

    def sim_menor():  # Função se for escolhida a opção "SIM" na primeira pergunta.

        pagina_vidro.pack_forget()  # "Esquece" a pagina antiga ou fecha a pagina antiga.

        pagina_sim_menor = ctk.CTkFrame(janela)  # Cria uma nova pagina
        pagina_sim_menor._set_appearance_mode("dark")
        pagina_sim_menor.pack(fill="both", expand=True)

        def nao_maior():  # Função se for escolhida a opção "NÃO" na segunda pergunta.

            pagina_sim_menor.pack_forget()  # "Esquece" a pagina antiga ou fecha a pagina antiga.

            pagina_receita_menor = ctk.CTkFrame(janela)  # Cria uma nova pagina
            pagina_receita_menor._set_appearance_mode("dark")
            pagina_receita_menor.pack(fill="both", expand=True)

            label_receitas = ctk.CTkLabel(pagina_receita_menor,
                                          text="Receita caso a garrafa tenha uma capacidade maior que 500 ml",
                                          font=("Arial", 24))
            label_receitas._set_appearance_mode("dark")
            label_receitas.pack(pady=50)

            botao_receita_menor(pagina_receita_menor, janela, menu, menu_func, voltar_func).pack(pady=10)

            botao_descarte = ctk.CTkButton(pagina_receita_menor, text="Descarte",
                                           # botao para ir a pagina de descarte caso o usuario nao queira fazer as receitas.
                                           command=lambda: descarte_lista(pagina_receita_menor, descarte))
            botao_descarte._set_appearance_mode("dark")
            botao_descarte.pack(pady=10)

            label_espaco = ctk.CTkLabel(pagina_receita_menor, text="")  # Label que cria um espaço na página.
            label_espaco._set_appearance_mode("dark")
            label_espaco.pack(side="bottom", pady=0)

            botao_fim = ctk.CTkButton(pagina_receita_menor, text="Fim", font=("Arial", 24), width=100,
                                      # Botão que avança para a página final.
                                      height=40, fg_color="Red", text_color="White",
                                      command=lambda: fim_receita(pagina_receita_menor, janela, menu, menu_func,
                                                                  voltar_func))
            botao_fim._set_appearance_mode("dark")
            botao_fim.pack(side="bottom", pady=5)

            botao_result_jornal_menu = ctk.CTkButton(pagina_receita_menor, text="Menu", font=("Arial", 24), width=100,
                                                     # botao para voltar ao menu inicial dentro da pagina temporaria.
                                                     height=40,
                                                     command=lambda: menu_func(pagina_receita_menor, menu))
            botao_result_jornal_menu._set_appearance_mode("dark")
            botao_result_jornal_menu.pack(side="bottom", pady=5)

            botao_result_jornal_voltar = ctk.CTkButton(pagina_receita_menor, text="Voltar", font=("Arial", 24),
                                                       # botao para voltar a pagina anterior dentro da pagina temporaria.
                                                       width=100, height=40,
                                                       command=lambda: voltar_func(pagina_receita_menor, pagina_vidro))
            botao_result_jornal_voltar._set_appearance_mode("dark")
            botao_result_jornal_voltar.pack(side="bottom", pady=5)

        def sim_maior():  # Função se for escolhida a opção "SIM" na segunda pergunta.

            pagina_sim_menor.pack_forget()  # "Esquece" a pagina antiga ou fecha a pagina antiga.

            pagina_sim_maior = ctk.CTkFrame(janela)  # Cria uma nova pagina
            pagina_sim_maior._set_appearance_mode("dark")
            pagina_sim_maior.pack(fill="both", expand=True)

            label_receitas = ctk.CTkLabel(pagina_sim_maior,
                                          text="Receita caso a garrafa tenha uma capacidade menor que 500 ml",
                                          font=("Arial", 24))
            label_receitas._set_appearance_mode("dark")
            label_receitas.pack(pady=50)

            botao_receita_menor(pagina_sim_maior, janela, menu, menu_func, voltar_func).pack(pady=10)

            label_receitas = ctk.CTkLabel(pagina_sim_maior,
                                          text="Receita caso a garrafa tenha uma capacidade maior que 500 ml",
                                          font=("Arial", 24))
            label_receitas._set_appearance_mode("dark")
            label_receitas.pack(pady=40)

            botao_receita_maior(pagina_sim_maior, janela, menu, menu_func, voltar_func).pack(pady=10)

            botao_descarte = ctk.CTkButton(pagina_sim_maior, text="Descarte",
                                           # botao para ir a pagina de descarte caso o usuario nao queira fazer as receitas.
                                           command=lambda: descarte_lista(pagina_sim_maior, descarte))
            botao_descarte._set_appearance_mode("dark")
            botao_descarte.pack(pady=30)

            label_espaco = ctk.CTkLabel(pagina_sim_maior, text="")  # Label que cria um espaço na página.
            label_espaco._set_appearance_mode("dark")
            label_espaco.pack(side="bottom", pady=0)

            botao_fim = ctk.CTkButton(pagina_sim_maior, text="Fim", font=("Arial", 24), width=100,
                                      # Botão que avança para a página final.
                                      height=40, fg_color="Red", text_color="White",
                                      command=lambda: fim_receita(pagina_sim_maior, janela, menu, menu_func,
                                                                  voltar_func))
            botao_fim._set_appearance_mode("dark")
            botao_fim.pack(side="bottom", pady=5)

            botao_result_vidro_menu = ctk.CTkButton(pagina_sim_maior, text="Menu", font=("Arial", 24), width=100,
                                                    # botao para voltar ao menu inicial dentro da pagina temporaria.
                                                    height=40,
                                                    command=lambda: menu_func(pagina_sim_maior, menu))
            botao_result_vidro_menu._set_appearance_mode("dark")
            botao_result_vidro_menu.pack(side="bottom", pady=5)

            botao_result_vidro_voltar = ctk.CTkButton(pagina_sim_maior, text="Voltar", font=("Arial", 24),
                                                      # botao para voltar a pagina anterior dentro da pagina temporaria.
                                                      width=100, height=40,
                                                      command=lambda: voltar_func(pagina_sim_maior, pagina_vidro))
            botao_result_vidro_voltar._set_appearance_mode("dark")
            botao_result_vidro_voltar.pack(side="bottom", pady=5)

        label_espaco = ctk.CTkLabel(pagina_sim_menor, text="",  # label para criar um espaço na pagina.
                                    font=("Arial", 24))
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(pady=170)

        label_maior = ctk.CTkLabel(pagina_sim_menor, # texto para fazer a segunda pergunta.
                                   text="Você tem alguma quantidade de garrafas de vidro maior que 500 ml de capacidade?",
                                   font=("Arial", 24))
        label_maior._set_appearance_mode("dark")
        label_maior.pack(pady=20)

        botao_vidro_sim_maior = ctk.CTkButton(pagina_sim_menor, text="SIM", width=200, command=sim_maior,  # Botão com a opção "SIM" que tem como comando a função sim_maior().
                                              fg_color="green")
        botao_vidro_sim_maior._set_appearance_mode("dark")
        botao_vidro_sim_maior.pack(pady=10)

        botao_vidro_nao_maior = ctk.CTkButton(pagina_sim_menor, text="NÃO", width=200, command=nao_maior,  # Botão com a opção "NÃO" que tem como comando a função nao_maior().
                                              fg_color="red")
        botao_vidro_nao_maior._set_appearance_mode("dark")
        botao_vidro_nao_maior.pack(pady=10)

        label_espaco_menor = ctk.CTkLabel(pagina_sim_menor, text="")  # Label que cria um espaço na página.
        label_espaco_menor._set_appearance_mode("dark")
        label_espaco_menor.pack(side="bottom", pady=0)

        botao_menu = ctk.CTkButton(pagina_sim_menor, text="Menu", font=("Arial", 24), width=100, height=40, # botao para voltar ao menu inicial dentro da pagina temporaria.
                                   command=lambda: menu_func(pagina_sim_menor, menu))
        botao_menu._set_appearance_mode("dark")
        botao_menu.pack(side="bottom", pady=5)

        botao_voltar = ctk.CTkButton(pagina_sim_menor, text="Voltar", font=("Arial", 24), width=100, height=40, # botao para voltar a pagina anterior dentro da pagina temporaria.
                                     command=lambda: voltar_func(pagina_sim_menor, pagina_vidro))
        botao_voltar._set_appearance_mode("dark")
        botao_voltar.pack(side="bottom", pady=5)

    label_vidro = ctk.CTkLabel(pagina_vidro, text="",  # label para criar um espaço na pagina.
                               font=("Arial", 24))
    label_vidro._set_appearance_mode("dark")
    label_vidro.pack(pady=170)

    label_pergunta = ctk.CTkLabel(pagina_vidro, width=300,  # texto para fazer a primeira pergunta.
                                  text="Você tem alguma quantidade de garrafas de vidro menor que 500 ml de capacidade?",
                                  font=("Arial", 24))
    label_pergunta._set_appearance_mode("dark")
    label_pergunta.pack(pady=20)

    botao_vidro_sim = ctk.CTkButton(pagina_vidro, text="SIM", width=200, command=sim_menor,  # Botão com a opção "SIM" que tem como comando a função sim_menor().
                                    fg_color="green")
    botao_vidro_sim._set_appearance_mode("dark")
    botao_vidro_sim.pack(pady=10)
    botao_vidro_nao = ctk.CTkButton(pagina_vidro, text="NÃO", width=200, command=nao_menor,  # Botão com a opção "SIM" que tem como comando a função nao_menor().
                                    fg_color="red")
    botao_vidro_nao._set_appearance_mode("dark")
    botao_vidro_nao.pack(pady=10)

    label_espaco_inicial = ctk.CTkLabel(pagina_vidro, text="")  # Label que cria um espaço na página.
    label_espaco_inicial._set_appearance_mode("dark")
    label_espaco_inicial.pack(side="bottom", pady=0)

    botao_vidro_menu = ctk.CTkButton(pagina_vidro, text="Menu", font=("Arial", 24), command=menu, width=100,  # Botão para voltar ao menu inicial.
                                     height=40)
    botao_vidro_menu._set_appearance_mode("dark")
    botao_vidro_menu.pack(side="bottom", pady=5)
    botao_vidro_voltar = ctk.CTkButton(pagina_vidro, text="Voltar", font=("Arial", 24), width=100, # Botão para voltar à pagina anterior.
                                       height=40, command=voltar)
    botao_vidro_voltar._set_appearance_mode("dark")
    botao_vidro_voltar.pack(side="bottom", pady=5)

    return pagina_vidro