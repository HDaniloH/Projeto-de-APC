import customtkinter as ctk
from tkinter import *
from receitas_papelao import *

lista_botao_receitas_caixa = [botao_receita_caixa, botao_receita_caixa2, botao_receita_caixa3, botao_receita_caixa4]
lista_botao_receitas_papelao = [botao_receita_papelao2, botao_receita_papelao]

def descarte_lista(pag_atual, descarte):
    pag_atual.pack_forget()
    descarte()

def nao_entry(entrada):     # Função para deletar o que esta escrito dentro da caixa de entrada
    entrada.delete(0, END)

def voltar_func(atual, anterior): # Função para voltar a pagina anterior dentro nas paginas temporarias do def
    atual.pack_forget()
    anterior.pack(fill="both", expand=True)

def menu_func(atual, menu): # Função para voltar ao menu dentro nas paginas temporarias do def
    atual.pack_forget()
    botao_menu_final = ctk.CTkButton(atual, text="Menu", command=menu())

def apagar(label): # Função para apagar uma label
    label.destroy()

def pag_papelao(janela, menu, papelao, caixa): # Função do menu do papelão.

    pagina_papelao = ctk.CTkFrame(janela) # Cria a página do menu do Papelão.
    pagina_papelao._set_appearance_mode("dark")

    label2 = ctk.CTkLabel(pagina_papelao, text="Escolha", font=("Arial", 24)) # Cria o texto do menu do papelão: "Escolha".
    label2._set_appearance_mode("dark")
    label2.pack(pady=50)

    botao_papelao = ctk.CTkButton(pagina_papelao, text="Papelão", command=papelao, fg_color="#8B4513", hover_color="#654321") # Botão para avançar para a pagina do papelão.
    botao_papelao._set_appearance_mode("dark")
    botao_papelao.pack(pady=20)

    botao_caixa_papelao = ctk.CTkButton(pagina_papelao, text="Caixa de Papelão", command=caixa, fg_color="#8B4513", hover_color="#654321") # Botão para avançar para a pagina da caixa de papelão.
    botao_caixa_papelao._set_appearance_mode("dark")
    botao_caixa_papelao.pack(pady=20)

    botao_papelao_menu = ctk.CTkButton(pagina_papelao, text="Menu", font=("Arial", 24), width=100, height=40, command=menu) # Botão para voltar ao menu.
    botao_papelao_menu._set_appearance_mode("dark")
    botao_papelao_menu.pack(side="bottom", pady=20)

    return pagina_papelao # retorna a pagina do menu do papelão.

def pag_papelao_escolha(janela, menu, voltar, descarte): #Função da página da escolha "Papelão".

    pagina_papelao_e_ = ctk.CTkFrame(janela) # Cria a página da escolha "Papelão".
    pagina_papelao_e_._set_appearance_mode("dark")

    def sim_entry():  # Função se for escolhida a opção "SIM" na pergunta de certeza.

        resultado_papelao = entry.get()  # Obtem a quantidade inserida no entry e a variavel recebe esse valor.

        """Processamento de dados:"""
        if resultado_papelao.isdigit() == False:  # Verifica se o valor da variavel é um digito inteiro.

            label_invalida = ctk.CTkLabel(pagina_papelao_e_,  # se nao for um digito inteiro este texto aparece na tela.
                                          text="Quantidade Invalida! Digite uma quantidade valida.",
                                          font=("Arial", 24), fg_color="#000000", corner_radius=10, height=40)
            label_invalida._set_appearance_mode("dark")
            label_invalida.pack(pady=50)
            pagina_papelao_e_.after(3000, apagar, label_invalida)  # apaga o texto depois de 3 segundos.

        elif resultado_papelao.isdigit() == True:  # Verifica se o valor da variavel é um digito inteiro.

            pagina_papelao_e_.pack_forget()  # "Esquece" a pagina antiga ou fecha a pagina antiga.

            pagina_papelao_lista = ctk.CTkFrame(janela)  # Cria uma nova pagina
            pagina_papelao_lista._set_appearance_mode("dark")
            pagina_papelao_lista.pack(fill="both", expand=True)

            label_receitas = ctk.CTkLabel(pagina_papelao_lista, text="Receitas", font=("Arial", 24))
            label_receitas._set_appearance_mode("dark")
            label_receitas.pack(pady=50)

            resultado_papelao = int(resultado_papelao)  # transforma o valor da variavel em inteiro.

            """Saída de dados:"""
            if resultado_papelao == 0:

                # Texto se o resultado for 0.

                label_triste = ctk.CTkLabel(pagina_papelao_lista, text=":(", font=("Arial", 40))
                label_triste._set_appearance_mode("dark")
                label_triste.pack(pady=20)

                label_juntar = ctk.CTkLabel(pagina_papelao_lista, text="Junte mais papelão", font=("Arial", 30))
                label_juntar._set_appearance_mode("dark")
                label_juntar.pack(pady=20)

                label_juntar2 = ctk.CTkLabel(pagina_papelao_lista,
                                             text="ou pegue mais com vizinhos/amigos/familiares.",
                                             font=("Arial", 30))
                label_juntar2._set_appearance_mode("dark")
                label_juntar2.pack(pady=20)

                label_obrigado = ctk.CTkLabel(pagina_papelao_lista,
                                              text="Agradeçemos por usar o nosso programa, Volte novamente!",
                                              font=("Arial", 30))
                label_obrigado._set_appearance_mode("dark")
                label_obrigado.pack(pady=20)

            if 0 < resultado_papelao < 4:  # verifica o valor da variavel.

                # Receitas se tiver apenas uma quantidade:

                lista_botao_receitas_papelao[0](pagina_papelao_lista, janela, menu, menu_func, voltar_func).pack( # Mostra o botão das receitas na página.
                    pady=10)

                botao_descarte = ctk.CTkButton(pagina_papelao_lista, text="Descarte", # botao para ir a pagina de descarte caso o usuario nao queira fazer as receitas.
                                               command=lambda: descarte_lista(pagina_papelao_lista, descarte))
                botao_descarte._set_appearance_mode("dark")
                botao_descarte.pack(pady=10)

            if resultado_papelao >= 4:  # verifica o valor da variavel.

                # Receitas se tiver apenas uma quantidade:

                for i in range(len(lista_botao_receitas_papelao)):
                    lista_botao_receitas_papelao[i](pagina_papelao_lista, janela, menu, menu_func, voltar_func).pack( # Mostra o botão das receitas na página.
                        pady=10)

                botao_descarte = ctk.CTkButton(pagina_papelao_lista, text="Descarte", # botao para ir a pagina de descarte caso o usuario nao queira fazer as receitas.
                                               command=lambda: descarte_lista(pagina_papelao_lista, descarte))
                botao_descarte._set_appearance_mode("dark")
                botao_descarte.pack(pady=10)

            label_espaco = ctk.CTkLabel(pagina_papelao_lista, text="")  # Label que cria um espaço na página.
            label_espaco._set_appearance_mode("dark")
            label_espaco.pack(side="bottom", pady=0)

            botao_fim = ctk.CTkButton(pagina_papelao_lista, text="Fim", font=("Arial", 24), width=100, # botão para avançar para a pagina final.
                                      height=40, fg_color="Red", text_color="White",
                                      command=lambda: fim_receita(pagina_papelao_lista, janela, menu, menu_func,
                                                                  voltar_func))
            botao_fim._set_appearance_mode("dark")
            botao_fim.pack(side="bottom", pady=5)

            botao_result_rolo_menu = ctk.CTkButton(pagina_papelao_lista, text="Menu", font=("Arial", 24), # botao para voltar ao menu inicial dentro da pagina temporaria.
                                                   width=100, height=40,
                                                   command=lambda: menu_func(pagina_papelao_lista, menu))
            botao_result_rolo_menu._set_appearance_mode("dark")
            botao_result_rolo_menu.pack(side="bottom", pady=5)

            botao_result_rolo_voltar = ctk.CTkButton(pagina_papelao_lista, text="Voltar", font=("Arial", 24), # botao para voltar a pagina anterior dentro da pagina temporaria.
                                                     width=100, height=40,
                                                     command=lambda: voltar_func(pagina_papelao_lista,
                                                                                 pagina_papelao_e_))
            botao_result_rolo_voltar._set_appearance_mode("dark")
            botao_result_rolo_voltar.pack(side="bottom", pady=5)

    label_menor_entry = ctk.CTkLabel(pagina_papelao_e_,  # Texto que pede para digitar a quantidade de papelão.
                                     text="Digite a quantidade de papelão que você tem",
                                     font=("Arial", 24))
    label_menor_entry._set_appearance_mode("dark")
    label_menor_entry.pack(pady=50)

    """Entrada de dados:"""
    entry = ctk.CTkEntry(pagina_papelao_e_, width=300,
                         placeholder_text="Digite aqui a quantidade...")
    entry._set_appearance_mode("dark")
    entry.pack()

    label_certeza_entry = ctk.CTkLabel(pagina_papelao_e_, width=300, text="Tem certeza?", # Texto para perguntar se o usuario tem certeza que quer avançar
                                       font=("Arial", 24))
    label_certeza_entry._set_appearance_mode("dark")
    label_certeza_entry.pack(pady=20)

    botao_papelao_sim_entry = ctk.CTkButton(pagina_papelao_e_, text="SIM", width=300, command=sim_entry, # Botão com a opção "SIM" que tem como comando a função sim_entry().
                                            fg_color="green")
    botao_papelao_sim_entry._set_appearance_mode("dark")
    botao_papelao_sim_entry.pack(pady=10)
    botao_papelao_nao_entry = ctk.CTkButton(pagina_papelao_e_, text="NÃO", width=300, # Botão com a opção "NÃO" que tem como comando a função nao_entry().
                                            command=lambda: nao_entry(entry),
                                            fg_color="red")
    botao_papelao_nao_entry._set_appearance_mode("dark")
    botao_papelao_nao_entry.pack(pady=10)

    label_espaco_papelao = ctk.CTkLabel(pagina_papelao_e_, text="")  # Label que cria um espaço na página.
    label_espaco_papelao._set_appearance_mode("dark")
    label_espaco_papelao.pack(side="bottom", pady=0)

    botao_papelao_e_menu = ctk.CTkButton(pagina_papelao_e_, text="Menu", font=("Arial", 24), command=menu, width=100, # Botão para voltar ao menu inicial.
                                         height=40)
    botao_papelao_e_menu._set_appearance_mode("dark")
    botao_papelao_e_menu.pack(side="bottom", pady=5)

    botao_papelao_voltar = ctk.CTkButton(pagina_papelao_e_, text="Voltar", font=("Arial", 24), command=voltar, # Botão para voltar à pagina anterior.
                                         width=100, height=40)
    botao_papelao_voltar._set_appearance_mode("dark")
    botao_papelao_voltar.pack(side="bottom", pady=5)

    return pagina_papelao_e_ #retorna a pagina da escolha papelão.

def pag_caixa(janela, menu, voltar, descarte): #função da página da escolha "Caixa".

    pagina_caixa = ctk.CTkFrame(janela) # Cria a página da escolha "Caixa".
    pagina_caixa._set_appearance_mode("dark")

    def sim(): # função se a opção sim for selecionada.

        resultado = entry.get() # Obtem a quantidade inserida no entry e a variavel recebe esse valor.

        """Processamento de dados:"""
        if resultado.isdigit() == False: # Verifica se o valor da variavel é um digito inteiro.

            label_invalida = ctk.CTkLabel(pagina_caixa, # se nao for um digito inteiro este texto aparece na tela.
                                          text="Quantidade Invalida! Digite uma quantidade valida.",
                                          font=("Arial", 24), fg_color="#000000", corner_radius=10, height=40)
            label_invalida._set_appearance_mode("dark")
            label_invalida.pack(pady=50)
            pagina_caixa.after(3000, apagar, label_invalida)  # apaga o texto depois de 3 segundos.

        if resultado.isdigit() == True:  # Verifica se o valor da variavel é um digito inteiro.

            pagina_caixa.pack_forget()  # "Esquece" a pagina antiga ou fecha a pagina antiga.

            pagina_lista_caixa = ctk.CTkFrame(janela)  # cria uma nova pagina
            pagina_lista_caixa._set_appearance_mode("dark")
            pagina_lista_caixa.pack(fill="both", expand=True)

            label_receitas = ctk.CTkLabel(pagina_lista_caixa, text="Receitas", font=("Arial", 24))
            label_receitas._set_appearance_mode("dark")
            label_receitas.pack(pady=50)

            resultado = int(resultado)  # transforma o valor da variavel em inteiro.

            """Saída de dados:"""

            if resultado == 0:

                # Texto se o resultado for 0.

                label_triste = ctk.CTkLabel(pagina_lista_caixa, text=":(", font=("Arial", 40))
                label_triste._set_appearance_mode("dark")
                label_triste.pack(pady=20)

                label_juntar = ctk.CTkLabel(pagina_lista_caixa, text="Junte mais caixas", font=("Arial", 30))
                label_juntar._set_appearance_mode("dark")
                label_juntar.pack(pady=20)

                label_juntar2 = ctk.CTkLabel(pagina_lista_caixa,
                                             text="ou pegue mais com vizinhos/amigos/familiares.",
                                             font=("Arial", 30))
                label_juntar2._set_appearance_mode("dark")
                label_juntar2.pack(pady=20)

                label_obrigado = ctk.CTkLabel(pagina_lista_caixa,
                                              text="Agradeçemos por usar o nosso programa, Volte novamente!",
                                              font=("Arial", 30))
                label_obrigado._set_appearance_mode("dark")
                label_obrigado.pack(pady=20)

            if resultado > 0:  # verifica o valor da variavel.

                # Receitas se tiver apenas uma quantidade:
                if resultado < 5:
                    for i in range(resultado):
                        lista_botao_receitas_caixa[i](pagina_lista_caixa, janela, menu, menu_func, voltar_func).pack(pady=10) # Mostra o botão das receitas na página.

                else:
                    for i in range(len(lista_botao_receitas_caixa)):
                        lista_botao_receitas_caixa[i](pagina_lista_caixa, janela, menu, menu_func, voltar_func).pack(pady=10) # Mostra o botão das receitas na página.



                botao_descarte = ctk.CTkButton(pagina_lista_caixa, text="Descarte", # botao para ir a pagina de descarte caso o usuario nao queira fazer as receitas.
                                               command=lambda: descarte_lista(pagina_lista_caixa, descarte))
                botao_descarte._set_appearance_mode("dark")
                botao_descarte.pack(pady=10)

            label_espaco = ctk.CTkLabel(pagina_lista_caixa, text="")  # Label que cria um espaço na página.
            label_espaco._set_appearance_mode("dark")
            label_espaco.pack(side="bottom", pady=0)

            botao_fim = ctk.CTkButton(pagina_lista_caixa, text="Fim", font=("Arial", 24), width=100, # botão para avançar para a pagina final.
                                                    height=40, fg_color="Red", text_color="White",
                                                    command=lambda: fim_receita(pagina_lista_caixa, janela, menu, menu_func, voltar_func))
            botao_fim._set_appearance_mode("dark")
            botao_fim.pack(side="bottom", pady=5)

            botao_result_caixa_menu = ctk.CTkButton(pagina_lista_caixa, text="Menu", font=("Arial", 24), width=100, # botao para voltar ao menu inicial dentro da pagina temporaria.
                                                    height=40,
                                                    command=lambda: menu_func(pagina_lista_caixa, menu))
            botao_result_caixa_menu._set_appearance_mode("dark")
            botao_result_caixa_menu.pack(side="bottom", pady=5)

            botao_result_caixa_voltar = ctk.CTkButton(pagina_lista_caixa, text="Voltar", font=("Arial", 24), width=100, # botao para voltar a pagina anterior dentro da pagina temporaria.
                                                      height=40, command=lambda: voltar_func(pagina_lista_caixa, pagina_caixa))
            botao_result_caixa_voltar._set_appearance_mode("dark")
            botao_result_caixa_voltar.pack(side="bottom", pady=5)

    label_caixa = ctk.CTkLabel(pagina_caixa, text="Caixa de Papelão",  # Cria o texto da pagina da Caixa de Papelão: "Caixa de Papelão".
                               font=("Arial", 24))
    label_caixa._set_appearance_mode("dark")
    label_caixa.pack(pady=50)

    label_pergunta = ctk.CTkLabel(pagina_caixa, width=300, text="Quantas caixas de papelão você tem?", # Texto para perguntar a quantidade de caixas de papelão.
                                  font=("Arial", 24))
    label_pergunta._set_appearance_mode("dark")
    label_pergunta.pack(pady=20)

    """Entrada de dados:"""
    entry = ctk.CTkEntry(pagina_caixa, width=300, placeholder_text="Digite aqui a quantidade...")
    entry._set_appearance_mode("dark")
    entry.pack()

    label_certeza = ctk.CTkLabel(pagina_caixa, width=300, text="Tem certeza?", # Texto para perguntar se o usuario tem certeza que quer avançar
                                 font=("Arial", 24))
    label_certeza._set_appearance_mode("dark")
    label_certeza.pack(pady=20)

    botao_caixa_entry_sim = ctk.CTkButton(pagina_caixa, text="SIM", width=300, command=sim, # Botão com a opção "SIM" que tem como comando a função sim().
                                          fg_color="green")
    botao_caixa_entry_sim._set_appearance_mode("dark")
    botao_caixa_entry_sim.pack(pady=10)
    botao_caixa_entry_nao = ctk.CTkButton(pagina_caixa, text="NÃO", width=300, command=lambda: nao_entry(entry), # Botão com a opção "NÃO" que tem como comando a função nao_entry().
                                          fg_color="red")
    botao_caixa_entry_nao._set_appearance_mode("dark")
    botao_caixa_entry_nao.pack(pady=10)

    label_espaco = ctk.CTkLabel(pagina_caixa, text="")  # Label que cria um espaço na página.
    label_espaco._set_appearance_mode("dark")
    label_espaco.pack(side="bottom", pady=0)

    botao_caixa_menu = ctk.CTkButton(pagina_caixa, text="Menu", font=("Arial", 24), width=100, height=40, # Botão para voltar ao menu inicial.
                                     command=menu)
    botao_caixa_menu._set_appearance_mode("dark")
    botao_caixa_menu.pack(side="bottom", pady=5)
    botao_caixa_voltar = ctk.CTkButton(pagina_caixa, text="Voltar", font=("Arial", 24), width=100, height=40, # Botão para voltar a pagina anterior.
                                       command=voltar)
    botao_caixa_voltar._set_appearance_mode("dark")
    botao_caixa_voltar.pack(side="bottom", pady=5)

    return pagina_caixa #retorna a pagina da caixa.