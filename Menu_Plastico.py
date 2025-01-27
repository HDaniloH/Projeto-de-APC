import customtkinter as ctk
from tkinter import *

def nao_entry(entrada): #Função para deletar o que esta escrito dentro da caixa de entrada
    entrada.delete(0, END)

def voltar_func(atual, anterior): #Função para voltar a pagina anterior dentro nas paginas temporarias do def
    atual.pack_forget()
    anterior.pack(fill="both", expand=True)

def menu_func(atual, menu): #Função para voltar ao menu dentro nas paginas temporarias do def
    atual.pack_forget()
    botao_menu_final = ctk.CTkButton(atual, text="Menu", command=menu())

def apagar(label): #Função para apagar uma label
    label.destroy()

def pag_plastico(janela, menu, garrafa_pet, tampa): # Função do menu do plástico.

    pagina_plastico_escolha = ctk.CTkFrame(janela) # Cria a página do menu do plástico.
    pagina_plastico_escolha._set_appearance_mode("dark")

    label2 = ctk.CTkLabel(pagina_plastico_escolha, text="Escolha", font=("Arial", 24)) # Cria o texto do menu do plastico: "Escolha".
    label2._set_appearance_mode("dark")
    label2.pack(pady=50)

    botao_plastico = ctk.CTkButton(pagina_plastico_escolha, text="Garrafa PET", command=garrafa_pet, fg_color="#A7C7E7", text_color="black", hover_color="#B0E0E6") # Botão para avançar para a pagina da garrafa PET.
    botao_plastico._set_appearance_mode("dark")
    botao_plastico.pack(pady=20)

    botao_tampas = ctk.CTkButton(pagina_plastico_escolha, text="Tampa de Garrafa", command=tampa, fg_color="#A7C7E7", text_color="black", hover_color="#B0E0E6") # Botão para avançar para a página das tampas de garrafa.
    botao_tampas._set_appearance_mode("dark")
    botao_tampas.pack(pady=20)

    botao_plastico_menu = ctk.CTkButton(pagina_plastico_escolha, text="Menu", font=("Arial", 24), width=100, height=40, command=menu) # Botão para voltar ao menu.
    botao_plastico_menu._set_appearance_mode("dark")
    botao_plastico_menu.pack(side="bottom", pady=20)

    return pagina_plastico_escolha


def pag_garrafa_PET(janela, menu, voltar): # Função da página da garrafa PET

    pagina_garrafa_pet = ctk.CTkFrame(janela)  # Cria a pagina da garrafa PET.
    pagina_garrafa_pet._set_appearance_mode("dark")

    def sim():  # Função se for escolhida a opção "SIM" na pergunta de certeza.

        resultado = entry.get()  # Obtem a quantidade inserida no entry e a variavel recebe esse valor.

        """Processamento de dados:"""
        if resultado.isdigit() == False:  # Verifica se o valor da variavel é um digito inteiro.

            label_invalida = ctk.CTkLabel(pagina_garrafa_pet, # se nao for um digito inteiro este texto aparece na tela.
                                          text="Quantidade Invalida! Digite uma quantidade valida.",
                                          font=("Arial", 24), fg_color="#000000", corner_radius=10, height=40)
            label_invalida._set_appearance_mode("dark")
            label_invalida.pack(pady=50)
            pagina_garrafa_pet.after(3000, apagar, label_invalida)  # apaga o texto depois de 3 segundos.

        if resultado.isdigit() == True:  # Verifica se o valor da variavel é um digito inteiro.

            pagina_garrafa_pet.pack_forget()  # "Esquece" a pagina antiga ou fecha a pagina antiga.

            pagina_lista_garrafa = ctk.CTkFrame(janela)  # Cria uma nova pagina
            pagina_lista_garrafa._set_appearance_mode("dark")
            pagina_lista_garrafa.pack(fill="both", expand=True)

            resultado = int(resultado)  # transforma o valor da variavel em inteiro.

            """Saída de dados:"""
            if resultado == 1:  # verifica o valor da variavel.

                # Receitas se tiver apenas uma quantidade:
                label2 = ctk.CTkLabel(pagina_lista_garrafa, text="Você consegue fazer apenas uma receita",
                                      font=("Arial", 24))
                label2._set_appearance_mode("dark")
                label2.pack(pady=50)

                label3 = ctk.CTkLabel(pagina_lista_garrafa, text="Receita",
                                      font=("Arial", 24))
                label3._set_appearance_mode("dark")
                label3.pack(pady=20)

            if resultado == 2:  # verifica o valor da variavel.

                # Receitas se tiver 2 quantidades:
                label2 = ctk.CTkLabel(pagina_lista_garrafa, text="Você consegue fazer estas receitas:",
                                      font=("Arial", 24))
                label2._set_appearance_mode("dark")
                label2.pack(pady=50)
                label3 = ctk.CTkLabel(pagina_lista_garrafa, text="Receita 1", font=("Arial", 24))
                label3._set_appearance_mode("dark")
                label3.pack(pady=20)
                label4 = ctk.CTkLabel(pagina_lista_garrafa, text="Receita 2", font=("Arial", 24))
                label4._set_appearance_mode("dark")
                label4.pack(pady=20)

            botao_result_jornal_menu = ctk.CTkButton(pagina_lista_garrafa, text="Menu", font=("Arial", 24), width=100, # botao para voltar ao menu inicial dentro da pagina temporaria.
                                                     height=40,
                                                     command=lambda: menu_func(pagina_lista_garrafa, menu))
            botao_result_jornal_menu._set_appearance_mode("dark")
            botao_result_jornal_menu.pack(side="bottom", pady=30)
            botao_result_jornal_voltar = ctk.CTkButton(pagina_lista_garrafa, text="Voltar", font=("Arial", 24), # botao para voltar a pagina anterior dentro da pagina temporaria.
                                                       width=100, height=40,
                                                       command=lambda: voltar_func(pagina_lista_garrafa,
                                                                                   pagina_garrafa_pet))
            botao_result_jornal_voltar._set_appearance_mode("dark")
            botao_result_jornal_voltar.pack(side="bottom", pady=10)

    label_garrafas = ctk.CTkLabel(pagina_garrafa_pet, text="Garrafas PET",  # Cria o texto da pagina da Garrafa PET: "Garrafas PET".
                                  font=("Arial", 24))
    label_garrafas._set_appearance_mode("dark")
    label_garrafas.pack(pady=50)

    label_pergunta = ctk.CTkLabel(pagina_garrafa_pet, width=300, text="Quantas Garrafas PET você tem?", # Texto que pergunta a quantidade de Garrafas PET que o usuario tem.
                                  font=("Arial", 24))
    label_pergunta._set_appearance_mode("dark")
    label_pergunta.pack(pady=20)

    """Entrada de dados:"""
    entry = ctk.CTkEntry(pagina_garrafa_pet, width=300, placeholder_text="Digite aqui a quantidade...")
    entry._set_appearance_mode("dark")
    entry.pack()

    label_certeza = ctk.CTkLabel(pagina_garrafa_pet, width=300, text="Tem certeza?", # Texto para perguntar se o usuario tem certeza que quer avançar
                                 font=("Arial", 24))
    label_certeza._set_appearance_mode("dark")
    label_certeza.pack(pady=20)

    botao_garrafas_sim = ctk.CTkButton(pagina_garrafa_pet, text="SIM", width=300, command=sim, # Botão com a opção "SIM" que tem como comando a função sim().
                                       fg_color="green")
    botao_garrafas_sim._set_appearance_mode("dark")
    botao_garrafas_sim.pack(pady=10)
    botao_garrafas_nao = ctk.CTkButton(pagina_garrafa_pet, text="NÃO", width=300, command=nao_entry(entry), # Botão com a opção "SIM" que tem como comando a função nao_entry().
                                       fg_color="red")
    botao_garrafas_nao._set_appearance_mode("dark")
    botao_garrafas_nao.pack(pady=10)

    botao_garrafas_menu = ctk.CTkButton(pagina_garrafa_pet, text="Menu", font=("Arial", 24), width=100, height=40, # Botão para voltar ao menu inicial.
                                        command=menu)
    botao_garrafas_menu._set_appearance_mode("dark")
    botao_garrafas_menu.pack(side="bottom", pady=30)
    botao_garrafas_voltar = ctk.CTkButton(pagina_garrafa_pet, text="Voltar", font=("Arial", 24), width=100, # Botão para voltar à pagina anterior.
                                          height=40, command=voltar)
    botao_garrafas_voltar._set_appearance_mode("dark")
    botao_garrafas_voltar.pack(side="bottom", pady=10)
    return pagina_garrafa_pet


def pag_tampa(janela, menu, voltar):
    pagina_tampa = ctk.CTkFrame(janela)
    pagina_tampa._set_appearance_mode("dark")
    label_tampa = ctk.CTkLabel(pagina_tampa, text="Tampa de Garrafa", font=("Arial", 24))
    label_tampa._set_appearance_mode("dark")
    label_tampa.pack(pady=50)
    botao_tampa_voltar = ctk.CTkButton(pagina_tampa, text="Voltar", command=voltar)
    botao_tampa_voltar._set_appearance_mode("dark")
    botao_tampa_voltar.pack(pady=20)
    botao_tampa_menu = ctk.CTkButton(pagina_tampa, text="Menu", command=menu)
    botao_tampa_menu._set_appearance_mode("dark")
    botao_tampa_menu.pack(pady=20)
    return pagina_tampa