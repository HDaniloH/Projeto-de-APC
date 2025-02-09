import customtkinter as ctk
from tkinter import *
from receitas_papel import *

def descarte_lista(pag_atual, descarte):
    pag_atual.pack_forget()
    descarte()

lista_botao_receitas_rolo = [botao_receita_rolo, botao_receita_rolo2]
lista_botao_receitas_papel = [botao_receita_papel, botao_receita_papel2]
lista_botao_receitas_jornal = [botao_receita_jornal, botao_receita_jornal2]

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

def pag_papel(janela, menu, rolo, papel): #Função do menu de papel.

    pagina_papel = ctk.CTkFrame(janela) #Cria a pagina do menu do papel.
    pagina_papel._set_appearance_mode("dark")

    label2 = ctk.CTkLabel(pagina_papel, text="Escolha", font=("Arial", 24)) #Cria o texto do menu de papel: "Escolha".
    label2._set_appearance_mode("dark")
    label2.pack(pady=50)

    botao_papel = ctk.CTkButton(pagina_papel, text="Papel e Jornal", command=papel, fg_color="white", text_color="black", hover_color="grey") #Botão para avançar para a pagina do papel.
    botao_papel._set_appearance_mode("dark")
    botao_papel.pack(pady=20)

    botao_rolo_papel = ctk.CTkButton(pagina_papel, text="Rolo de Papel", command=rolo, fg_color="white", text_color="black", hover_color="grey") #Botão para avançar para a pagina do rolo de papel.
    botao_rolo_papel._set_appearance_mode("dark")
    botao_rolo_papel.pack(pady=20)

    botao_papel_menu = ctk.CTkButton(pagina_papel, text="Menu", font=("Arial", 24), width=100, height=40, command=menu) #Botão para voltar ao menu.
    botao_papel_menu._set_appearance_mode("dark")
    botao_papel_menu.pack(side="bottom", pady=20)

    return pagina_papel #Retorna a pagina do menu de papel.

def pag_rolo_papel(janela, menu, voltar, descarte): #Função da página do rolo de papel.
    def sim(): #função se a opção sim for selecionada.

        resultado = entry.get() #Obtem a quantidade inserida no entry e a variavel recebe esse valor.

        """Processamento de dados:"""
        if resultado.isdigit() == False: #Verifica se o valor da variavel é um digito inteiro.

            label_invalida = ctk.CTkLabel(pagina_rolo_papel, #se nao for um digito inteiro este texto aparece na tela.
                                          text="Quantidade Invalida! Digite uma quantidade valida.",
                                          font=("Arial", 24), fg_color="#000000", corner_radius=10, height=40)
            label_invalida._set_appearance_mode("dark")
            label_invalida.pack(pady=50)
            pagina_rolo_papel.after(3000, apagar, label_invalida) #apaga o texto depois de 3 segundos.

        if resultado.isdigit() == True: #Verifica se o valor da variavel é um digito inteiro.

            pagina_rolo_papel.pack_forget() #"Esquece" a pagina antiga ou fecha a pagina antiga.
            pagina_lista_rolo = ctk.CTkFrame(janela) #cria uma nova pagina
            pagina_lista_rolo._set_appearance_mode("dark")
            pagina_lista_rolo.pack(fill="both", expand=True)

            label_receitas = ctk.CTkLabel(pagina_lista_rolo, text="Receitas", font=("Arial", 24))
            label_receitas._set_appearance_mode("dark")
            label_receitas.pack(pady=50)

            resultado = int(resultado) #transforma o valor da variavel em inteiro.

            """Saída de dados:"""

            if resultado == 0:

                # Texto se o resultado for 0.

                label_triste = ctk.CTkLabel(pagina_lista_rolo, text=":(", font=("Arial", 40))
                label_triste._set_appearance_mode("dark")
                label_triste.pack(pady=20)

                label_juntar = ctk.CTkLabel(pagina_lista_rolo, text="Junte mais rolos de papel", font=("Arial", 30))
                label_juntar._set_appearance_mode("dark")
                label_juntar.pack(pady=20)

                label_juntar2 = ctk.CTkLabel(pagina_lista_rolo,
                                             text="ou pegue mais com vizinhos/amigos/familiares.",
                                             font=("Arial", 30))
                label_juntar2._set_appearance_mode("dark")
                label_juntar2.pack(pady=20)

                label_obrigado = ctk.CTkLabel(pagina_lista_rolo,
                                              text="Agradeçemos por usar o nosso programa, Volte novamente!",
                                              font=("Arial", 30))
                label_obrigado._set_appearance_mode("dark")
                label_obrigado.pack(pady=20)

            if resultado > 0:  # verifica o valor da variavel.

                # Receitas:
                if resultado < 3: # Se for menor que 3 ele mostra na pagina a quantidade de botões baseado no resultado.
                    for i in range(resultado):
                        lista_botao_receitas_rolo[i](pagina_lista_rolo, janela, menu, menu_func, voltar_func).pack(pady=10) # Mostra os botões na página.

                else: # Se não ele mostra todos os botões da lista.
                    for i in range(len(lista_botao_receitas_rolo)):
                        lista_botao_receitas_rolo[i](pagina_lista_rolo, janela, menu, menu_func, voltar_func).pack(pady=10) # Mostra os botões na página.

                botao_descarte = ctk.CTkButton(pagina_lista_rolo, text="Descarte", # botao para ir a pagina de descarte caso o usuario nao queira fazer as receitas.
                                               command=lambda: descarte_lista(pagina_lista_rolo, descarte))
                botao_descarte._set_appearance_mode("dark")
                botao_descarte.pack(pady=10)

            label_espaco_rolo_lista = ctk.CTkLabel(pagina_lista_rolo, text="")  # Label que cria um espaço na página.
            label_espaco_rolo_lista._set_appearance_mode("dark")
            label_espaco_rolo_lista.pack(side="bottom", pady=0)

            botao_fim = ctk.CTkButton(pagina_lista_rolo, text="Fim", font=("Arial", 24), width=100, # Botão que avança para a página final.
                                      height=40, fg_color="Red", text_color="White",
                                      command=lambda: fim_receita(pagina_lista_rolo, janela, menu, menu_func, voltar_func))
            botao_fim._set_appearance_mode("dark")
            botao_fim.pack(side="bottom", pady=5)

            botao_result_rolo_menu = ctk.CTkButton(pagina_lista_rolo, text="Menu", font=("Arial", 24), width=100, height=40, #botao para voltar ao menu inicial dentro da pagina temporaria.
                                                   command=lambda: menu_func(pagina_lista_rolo, menu))
            botao_result_rolo_menu._set_appearance_mode("dark")
            botao_result_rolo_menu.pack(side="bottom", pady=5)

            botao_result_rolo_voltar = ctk.CTkButton(pagina_lista_rolo, text="Voltar", font=("Arial", 24), width=100, height=40,  #botao para voltar a pagina anterior dentro da pagina temporaria.
                                                     command=lambda: voltar_func(pagina_lista_rolo, pagina_rolo_papel))
            botao_result_rolo_voltar._set_appearance_mode("dark")
            botao_result_rolo_voltar.pack(side="bottom", pady=5)

    pagina_rolo_papel = ctk.CTkFrame(janela) #Cria a pagina do rolo de papel.
    pagina_rolo_papel._set_appearance_mode("dark")

    label_rolo = ctk.CTkLabel(pagina_rolo_papel, text="Rolo de Papel", font=("Arial", 24)) #Cria o texto da pagina do rolo de papel: "Rolo de Papel".
    label_rolo._set_appearance_mode("dark")
    label_rolo.pack(pady=50)

    label_pergunta = ctk.CTkLabel(pagina_rolo_papel, width=300, text="Quantos rolos de papel você tem?", font=("Arial", 24)) #Texto para perguntar a quantidade de rolos.
    label_pergunta._set_appearance_mode("dark")
    label_pergunta.pack(pady=20)

    """Entrada de dados:"""
    entry = ctk.CTkEntry(pagina_rolo_papel, width=300, placeholder_text="Digite aqui a quantidade...")
    entry._set_appearance_mode("dark")
    entry.pack()

    label_certeza = ctk.CTkLabel(pagina_rolo_papel, width=300, text="Tem certeza?", font=("Arial", 24)) #Texto para perguntar se o usuario tem certeza que quer avançar
    label_certeza._set_appearance_mode("dark")
    label_certeza.pack(pady=20)

    botao_rolo_papel_sim = ctk.CTkButton(pagina_rolo_papel, text="SIM", width=300, command=sim, fg_color="green") #Botão com a opção "SIM" que tem como comando a função sim().
    botao_rolo_papel_sim._set_appearance_mode("dark")
    botao_rolo_papel_sim.pack(pady=10)

    botao_rolo_papel_nao = ctk.CTkButton(pagina_rolo_papel, text="NÃO", width= 300, command=lambda: nao_entry(entry), fg_color="red") #Botão com a opção "NÃO" que tem como comando a função nao_entry().
    botao_rolo_papel_nao._set_appearance_mode("dark")
    botao_rolo_papel_nao.pack(pady=10)

    label_espaco = ctk.CTkLabel(pagina_rolo_papel, text="")  # Label que cria um espaço na página.
    label_espaco._set_appearance_mode("dark")
    label_espaco.pack(side="bottom", pady=0)

    botao_rolo_papel_menu = ctk.CTkButton(pagina_rolo_papel, text="Menu", font=("Arial", 24), width=100, height=40, #Botão para voltar ao menu inicial.
                                          command=menu)
    botao_rolo_papel_menu._set_appearance_mode("dark")
    botao_rolo_papel_menu.pack(side="bottom", pady=5)

    botao_rolo_papel_voltar = ctk.CTkButton(pagina_rolo_papel, text="Voltar", font=("Arial", 24), width=100, height=40, #Botão para voltar a pagina anterior.
                                            command=voltar)
    botao_rolo_papel_voltar._set_appearance_mode("dark")
    botao_rolo_papel_voltar.pack(side="bottom", pady=5)

    return pagina_rolo_papel #Retorna a pagina do rolo de papel.

def pag_papel_escolha(janela, menu, voltar, descarte): #Função da página da escolha de papel.

    pagina_papel_escolha = ctk.CTkFrame(janela) #Cria a pagina da escolha de papel.
    pagina_papel_escolha._set_appearance_mode("dark")

    def nao_papel(): #Função se for escolhida a opção "NÃO" na primeira pergunta.

        pagina_papel_escolha.pack_forget() #"Esquece" a pagina antiga ou fecha a pagina antiga.
        pagina_nao_papel = ctk.CTkFrame(janela) #Cria uma nova pagina
        pagina_nao_papel._set_appearance_mode("dark")
        pagina_nao_papel.pack(fill="both", expand=True)

        def sim_entry_n(): #Função se for escolhida a opção "SIM" na pergunta de certeza.

            resultado = entry_maior_n.get() #Obtem a quantidade inserida no entry e a variavel recebe esse valor.

            """Processamento de dados:"""
            if resultado.isdigit() == False: #Verifica se o valor da variavel é um digito inteiro.

                label_invalida = ctk.CTkLabel(pagina_nao_papel,  #se nao for um digito inteiro este texto aparece na tela.
                                              text="Quantidade Invalida! Digite uma quantidade valida.",
                                              font=("Arial", 24), fg_color="#000000", corner_radius=10, height=40)
                label_invalida._set_appearance_mode("dark")
                label_invalida.pack(pady=50)
                pagina_nao_papel.after(3000, apagar, label_invalida) #apaga o texto depois de 3 segundos.

            elif resultado.isdigit() == True: #Verifica se o valor da variavel é um digito inteiro.

                pagina_nao_papel.pack_forget() #"Esquece" a pagina antiga ou fecha a pagina antiga.

                pagina_jornal_lista = ctk.CTkFrame(janela) #Cria uma nova pagina
                pagina_jornal_lista._set_appearance_mode("dark")
                pagina_jornal_lista.pack(fill="both", expand=True)

                label_receitas = ctk.CTkLabel(pagina_jornal_lista, text="Receitas", font=("Arial", 24))
                label_receitas._set_appearance_mode("dark")
                label_receitas.pack(pady=50)

                resultado = int(resultado) #transforma o valor da variavel em inteiro.

                """Saída de dados:"""

                if resultado == 0:

                    # Texto se o resultado for 0.

                    label_triste = ctk.CTkLabel(pagina_jornal_lista, text=":(", font=("Arial", 40))
                    label_triste._set_appearance_mode("dark")
                    label_triste.pack(pady=20)

                    label_juntar = ctk.CTkLabel(pagina_jornal_lista, text="Junte mais jornal", font=("Arial", 30))
                    label_juntar._set_appearance_mode("dark")
                    label_juntar.pack(pady=20)

                    label_juntar2 = ctk.CTkLabel(pagina_jornal_lista,
                                                 text="ou pegue mais com vizinhos/amigos/familiares.",
                                                 font=("Arial", 30))
                    label_juntar2._set_appearance_mode("dark")
                    label_juntar2.pack(pady=20)

                    label_obrigado = ctk.CTkLabel(pagina_jornal_lista,
                                                  text="Agradeçemos por usar o nosso programa, Volte novamente!",
                                                  font=("Arial", 30))
                    label_obrigado._set_appearance_mode("dark")
                    label_obrigado.pack(pady=20)

                if resultado > 0:  # verifica o valor da variavel.

                    # Receitas:
                    if resultado < 3: # Se for menor que 3 ele mostra na pagina a quantidade de botões baseado no resultado.
                        for i in range(resultado):
                            lista_botao_receitas_jornal[i](pagina_jornal_lista, janela, menu, menu_func, voltar_func).pack( # Mostra os botões na página.
                                pady=10)

                    else: # Se não ele mostra todos os botões da lista.
                        for i in range(len(lista_botao_receitas_jornal)):
                            lista_botao_receitas_jornal[i](pagina_jornal_lista, janela, menu, menu_func, voltar_func).pack( # Mostra os botões na página.
                                pady=10)

                    botao_descarte = ctk.CTkButton(pagina_jornal_lista, text="Descarte", # botao para ir a pagina de descarte caso o usuario nao queira fazer as receitas.
                                                   command=lambda: descarte_lista(pagina_jornal_lista, descarte))
                    botao_descarte._set_appearance_mode("dark")
                    botao_descarte.pack(pady=10)

                label_espaco_papel_lista = ctk.CTkLabel(pagina_jornal_lista,  # Label que cria um espaço na página.
                                                        text="")
                label_espaco_papel_lista._set_appearance_mode("dark")
                label_espaco_papel_lista.pack(side="bottom", pady=0)

                botao_fim = ctk.CTkButton(pagina_jornal_lista, text="Fim", font=("Arial", 24), width=100, # Botão que avança para a página final.
                                          height=40, fg_color="Red", text_color="White",
                                          command=lambda: fim_receita(pagina_jornal_lista, janela, menu, menu_func,
                                                                      voltar_func))
                botao_fim._set_appearance_mode("dark")
                botao_fim.pack(side="bottom", pady=5)

                botao_result_jornal_menu = ctk.CTkButton(pagina_jornal_lista, text="Menu", font=("Arial", 24), width=100, height=40, # botao para voltar ao menu inicial dentro da pagina temporaria.
                                                         command=lambda: menu_func(pagina_jornal_lista, menu))
                botao_result_jornal_menu._set_appearance_mode("dark")
                botao_result_jornal_menu.pack(side="bottom", pady=5)

                botao_result_jornal_voltar = ctk.CTkButton(pagina_jornal_lista, text="Voltar", font=("Arial", 24), width=100, height=40, # botao para voltar a pagina anterior dentro da pagina temporaria.
                                                           command=lambda: voltar_func(pagina_jornal_lista,
                                                                                       pagina_nao_papel))
                botao_result_jornal_voltar._set_appearance_mode("dark")
                botao_result_jornal_voltar.pack(side="bottom", pady=5)

        label_maior_m = ctk.CTkLabel(pagina_nao_papel, # Texto que pede para digitar a quantidade de folhas de jornal.
                                     text="Digite a quantidade de folhas de Jornal que você tem",
                                     font=("Arial", 24))
        label_maior_m._set_appearance_mode("dark")
        label_maior_m.pack(pady=50)

        """Entrada de dados:"""
        entry_maior_n = ctk.CTkEntry(pagina_nao_papel, width=300,
                                     placeholder_text="Digite aqui a quantidade...")
        entry_maior_n._set_appearance_mode("dark")
        entry_maior_n.pack()

        label_certeza_entry_n = ctk.CTkLabel(pagina_nao_papel, width=300, text="Tem certeza?", font=("Arial", 24)) # Texto para perguntar se o usuario tem certeza que quer avançar
        label_certeza_entry_n._set_appearance_mode("dark")
        label_certeza_entry_n.pack(pady=20)

        botao_jornal_sim_entry_n = ctk.CTkButton(pagina_nao_papel, text="SIM", width=300, command=sim_entry_n,  # Botão com a opção "SIM" que tem como comando a função sim_entry_n().
                                                 fg_color="green")
        botao_jornal_sim_entry_n._set_appearance_mode("dark")
        botao_jornal_sim_entry_n.pack(pady=10)
        botao_jornal_nao_entry_n = ctk.CTkButton(pagina_nao_papel, text="NÃO", width=300, command=lambda: nao_entry(entry_maior_n),  # Botão com a opção "NÃO" que tem como comando a função nao_entry().
                                                 fg_color="red")
        botao_jornal_nao_entry_n._set_appearance_mode("dark")
        botao_jornal_nao_entry_n.pack(pady=10)

        label_espaco_nao_papel = ctk.CTkLabel(pagina_nao_papel,  # Label que cria um espaço na página.
                                              text="")
        label_espaco_nao_papel._set_appearance_mode("dark")
        label_espaco_nao_papel.pack(side="bottom", pady=0)

        botao_menu2 = ctk.CTkButton(pagina_nao_papel, text="Menu", font=("Arial", 24), width=100, height=40,  # botao para voltar ao menu inicial dentro da pagina temporaria.
                                    command=lambda: menu_func(pagina_nao_papel, menu)
                                    )
        botao_menu2._set_appearance_mode("dark")
        botao_menu2.pack(side="bottom", pady=5)

        botao_voltar2 = ctk.CTkButton(pagina_nao_papel, text="Voltar", font=("Arial", 24), width=100, height=40,  # botao para voltar a pagina anterior dentro da pagina temporaria.
                                      command=lambda: voltar_func(pagina_nao_papel, pagina_papel_escolha)
                                      )
        botao_voltar2._set_appearance_mode("dark")
        botao_voltar2.pack(side="bottom", pady=5)

    def sim_papel(): # Função se for escolhida a opção "SIM" na primeira pergunta.

        pagina_papel_escolha.pack_forget()  # "Esquece" a pagina antiga ou fecha a pagina antiga.

        pagina_sim_papel = ctk.CTkFrame(janela) # Cria uma nova pagina
        pagina_sim_papel._set_appearance_mode("dark")
        pagina_sim_papel.pack(fill="both", expand=True)

        def nao_jornal(): # Função se for escolhida a opção "NÃO" na segunda pergunta.

            pagina_sim_papel.pack_forget() # "Esquece" a pagina antiga ou fecha a pagina antiga.

            pagina_nao_jornal = ctk.CTkFrame(janela) # Cria uma nova pagina
            pagina_nao_jornal._set_appearance_mode("dark")
            pagina_nao_jornal.pack(fill="both", expand=True)

            def sim_entry(): # Função se for escolhida a opção "SIM" na pergunta de certeza.

                resultado_papel = entry.get() # Obtem a quantidade inserida no entry e a variavel recebe esse valor.

                """Processamento de dados:"""
                if resultado_papel.isdigit() == False: # Verifica se o valor da variavel é um digito inteiro.

                    label_invalida = ctk.CTkLabel(pagina_nao_jornal,  # se nao for um digito inteiro este texto aparece na tela.
                                                  text="Quantidade Invalida! Digite uma quantidade valida.",
                                                  font=("Arial", 24), fg_color="#000000", corner_radius=10, height=40)
                    label_invalida._set_appearance_mode("dark")
                    label_invalida.pack(pady=50)
                    pagina_nao_jornal.after(3000, apagar, label_invalida) # apaga o texto depois de 3 segundos.

                elif resultado_papel.isdigit() == True: # Verifica se o valor da variavel é um digito inteiro.

                    pagina_nao_jornal.pack_forget() # "Esquece" a pagina antiga ou fecha a pagina antiga.

                    pagina_papel_lista = ctk.CTkFrame(janela) # Cria uma nova pagina
                    pagina_papel_lista._set_appearance_mode("dark")
                    pagina_papel_lista.pack(fill="both", expand=True)

                    label_receitas = ctk.CTkLabel(pagina_papel_lista, text="Receitas", font=("Arial", 24))
                    label_receitas._set_appearance_mode("dark")
                    label_receitas.pack(pady=50)

                    resultado_papel = int(resultado_papel) # transforma o valor da variavel em inteiro.

                    """Saída de dados:"""

                    if resultado_papel == 0:

                        #texto se o resultado_papel for 0.

                        label_triste = ctk.CTkLabel(pagina_papel_lista, text=":(", font=("Arial", 40))
                        label_triste._set_appearance_mode("dark")
                        label_triste.pack(pady=20)

                        label_juntar = ctk.CTkLabel(pagina_papel_lista, text="Junte mais papel", font=("Arial", 30))
                        label_juntar._set_appearance_mode("dark")
                        label_juntar.pack(pady=20)

                        label_juntar2 = ctk.CTkLabel(pagina_papel_lista,
                                                     text="ou pegue mais com vizinhos/amigos/familiares.",
                                                     font=("Arial", 30))
                        label_juntar2._set_appearance_mode("dark")
                        label_juntar2.pack(pady=20)

                        label_obrigado = ctk.CTkLabel(pagina_papel_lista,
                                                      text="Agradeçemos por usar o nosso programa, Volte novamente!",
                                                      font=("Arial", 30))
                        label_obrigado._set_appearance_mode("dark")
                        label_obrigado.pack(pady=20)

                    if resultado_papel > 0:  # verifica o valor da variavel.

                        # Receitas:
                        if resultado_papel < 3: # Se for menor que 3 ele mostra na pagina a quantidade de botões baseado no resultado_papel.
                            for i in range(resultado_papel):
                                lista_botao_receitas_papel[i](pagina_papel_lista, janela, menu, menu_func, # Mostra os botões na página.
                                                               voltar_func).pack(
                                    pady=10)

                        else: # Se não ele mostra na pagina todos os botões da lista.
                            for i in range(len(lista_botao_receitas_papel)):
                                lista_botao_receitas_papel[i](pagina_papel_lista, janela, menu, menu_func, # Mostra os botões na página.
                                                               voltar_func).pack(
                                    pady=10)

                        botao_descarte = ctk.CTkButton(pagina_papel_lista, text="Descarte", # botao para ir a pagina de descarte caso o usuario nao queira fazer as receitas.
                                                       command=lambda: descarte_lista(pagina_papel_lista, descarte))
                        botao_descarte._set_appearance_mode("dark")
                        botao_descarte.pack(pady=10)

                    label_espaco_papel_lista = ctk.CTkLabel(pagina_papel_lista,  # Label que cria um espaço na página.
                                                            text="")
                    label_espaco_papel_lista._set_appearance_mode("dark")
                    label_espaco_papel_lista.pack(side="bottom", pady=0)

                    botao_fim = ctk.CTkButton(pagina_papel_lista, text="Fim", font=("Arial", 24), width=100,
                                              # Botão que avança para a página final.
                                              height=40, fg_color="Red", text_color="White",
                                              command=lambda: fim_receita(pagina_papel_lista, janela, menu, menu_func,
                                                                          voltar_func))
                    botao_fim._set_appearance_mode("dark")
                    botao_fim.pack(side="bottom", pady=5)

                    botao_result_papel_menu = ctk.CTkButton(pagina_papel_lista, text="Menu", font=("Arial", 24), width=100, height=40,  # botao para voltar ao menu inicial dentro da pagina temporaria.
                                                            command=lambda: menu_func(pagina_papel_lista, menu))
                    botao_result_papel_menu._set_appearance_mode("dark")
                    botao_result_papel_menu.pack(side ="bottom", pady=5)

                    botao_result_papel_voltar = ctk.CTkButton(pagina_papel_lista, text="Voltar", font=("Arial", 24), width=100, height=40,  # botao para voltar a pagina anterior dentro da pagina temporaria.
                                                              command=lambda: voltar_func(pagina_papel_lista, pagina_nao_jornal))
                    botao_result_papel_voltar._set_appearance_mode("dark")
                    botao_result_papel_voltar.pack(side ="bottom", pady=5)

            label_menor_entry = ctk.CTkLabel(pagina_nao_jornal,
                                             text="Digite a quantidade de papel que você tem",
                                             font=("Arial", 24))
            label_menor_entry._set_appearance_mode("dark")
            label_menor_entry.pack(pady=50)

            """Entrada de dados:"""
            entry = ctk.CTkEntry(pagina_nao_jornal, width=300,
                                 placeholder_text="Digite aqui a quantidade...")
            entry._set_appearance_mode("dark")
            entry.pack()

            label_certeza_entry = ctk.CTkLabel(pagina_nao_jornal, width=300, text="Tem certeza?", font=("Arial", 24)) # Texto para perguntar se o usuario tem certeza que quer avançar
            label_certeza_entry._set_appearance_mode("dark")
            label_certeza_entry.pack(pady=20)

            botao_papel_sim_entry = ctk.CTkButton(pagina_nao_jornal, text="SIM", width=300, command=sim_entry,  # Botão com a opção "SIM" que tem como comando a função sim_entry().
                                                  fg_color="green")
            botao_papel_sim_entry._set_appearance_mode("dark")
            botao_papel_sim_entry.pack(pady=10)
            botao_papel_nao_entry = ctk.CTkButton(pagina_nao_jornal, text="NÃO", width=300, command=lambda: nao_entry(entry),  # Botão com a opção "NÃO" que tem como comando a função nao_entry().
                                                  fg_color="red")
            botao_papel_nao_entry._set_appearance_mode("dark")
            botao_papel_nao_entry.pack(pady=10)

            label_espaco_nao_maior = ctk.CTkLabel(pagina_nao_jornal,  # Label que cria um espaço na página.
                                                  text="")
            label_espaco_nao_maior._set_appearance_mode("dark")
            label_espaco_nao_maior.pack(side="bottom", pady=0)

            botao_menu2 = ctk.CTkButton(pagina_nao_jornal, text="Menu", font=("Arial", 24), width=100, height=40,  # botao para voltar ao menu inicial dentro da pagina temporaria.
                                        command=lambda: menu_func(pagina_nao_jornal, menu))
            botao_menu2._set_appearance_mode("dark")
            botao_menu2.pack(side= "bottom", pady=5)

            botao_voltar2 = ctk.CTkButton(pagina_nao_jornal, text="Voltar", font=("Arial", 24), width=100, height=40,  # botao para voltar a pagina anterior dentro da pagina temporaria.
                                          command=lambda: voltar_func(pagina_nao_jornal, pagina_sim_papel))
            botao_voltar2._set_appearance_mode("dark")
            botao_voltar2.pack(side= "bottom", pady=5)

        def sim_jornal(): # Função se for escolhida a opção "SIM" na segunda pergunta.

            pagina_sim_papel.pack_forget() # "Esquece" a pagina antiga ou fecha a pagina antiga.

            pagina_sim_jornal = ctk.CTkFrame(janela) # Cria uma nova pagina
            pagina_sim_jornal._set_appearance_mode("dark")
            pagina_sim_jornal.pack(fill="both", expand=True)

            def nao_entry_plus(): # Função para deletar o que esta escrito dentro das duas caixas de entrada.
                entry_papel.delete(0, END)
                entry_jornal.delete(0, END)

            def sim_entry(): # Função se for escolhida a opção "SIM" na pergunta de certeza.

                resultado_papel = entry_papel.get() # Obtem a quantidade inserida no primeiro entry e a variavel recebe esse valor.
                resultado_jornal = entry_jornal.get() # Obtem a quantidade inserida no segundo entry e a variavel recebe esse valor.

                """Processamento de dados:"""
                if resultado_papel.isdigit() == False: # Verifica se o valor da primeira variavel é um digito inteiro.

                    label_invalida = ctk.CTkLabel(pagina_sim_jornal,  # se nao for um digito inteiro este texto aparece na tela.
                                                  text="A Primeira Quantidade está Invalida! Digite uma quantidade valida.",
                                                  font=("Arial", 24), fg_color="#000000", corner_radius=10, height=40)
                    label_invalida._set_appearance_mode("dark")
                    label_invalida.pack(pady=50)
                    pagina_sim_jornal.after(3000, apagar, label_invalida) # apaga o texto depois de 3 segundos.

                if resultado_jornal.isdigit() == False: # Verifica se o valor da segunda variavel é um digito inteiro.

                    label_invalida2 = ctk.CTkLabel(pagina_sim_jornal,  #se nao for um digito inteiro este texto aparece na tela.
                                                   text="A Segunda Quantidade está Invalida! Digite uma quantidade valida.",
                                                   font=("Arial", 24), fg_color="#000000", corner_radius=10, height=40)

                    label_invalida2._set_appearance_mode("dark")
                    label_invalida2.pack(pady=50)
                    pagina_sim_jornal.after(3000, apagar, label_invalida2) # apaga o texto depois de 3 segundos.

                elif resultado_papel.isdigit() == True and resultado_jornal.isdigit() == True: # Verifica se o valor das duas variaveis é um digito inteiro.

                    pagina_sim_jornal.pack_forget() # "Esquece" a pagina antiga ou fecha a pagina antiga.

                    pagina_folhas_lista = ctk.CTkFrame(janela) #Cria uma nova pagina
                    pagina_folhas_lista._set_appearance_mode("dark")
                    pagina_folhas_lista.pack(fill="both", expand=True)

                    resultado_papel = int(resultado_papel) # transforma o valor da variavel em inteiro.
                    resultado_jornal = int(resultado_jornal) # transforma o valor da variavel em inteiro.

                    """Saída de dados:"""

                    if resultado_papel == 0 and resultado_jornal == 0:

                        # Texto se o resultado das duas variaveis for 0.

                        label_triste_espaco = ctk.CTkLabel(pagina_folhas_lista, text="", font=("Arial", 40))
                        label_triste_espaco._set_appearance_mode("dark")
                        label_triste_espaco.pack(pady=50)

                        label_triste = ctk.CTkLabel(pagina_folhas_lista, text=":(", font=("Arial", 40))
                        label_triste._set_appearance_mode("dark")
                        label_triste.pack(pady=20)

                        label_juntar = ctk.CTkLabel(pagina_folhas_lista, text="Junte mais papel e jornal", font=("Arial", 30))
                        label_juntar._set_appearance_mode("dark")
                        label_juntar.pack(pady=20)

                        label_juntar2 = ctk.CTkLabel(pagina_folhas_lista,
                                                     text="ou pegue mais com vizinhos/amigos/familiares.",
                                                     font=("Arial", 30))
                        label_juntar2._set_appearance_mode("dark")
                        label_juntar2.pack(pady=20)

                        label_obrigado = ctk.CTkLabel(pagina_folhas_lista,
                                                      text="Agradeçemos por usar o nosso programa, Volte novamente!",
                                                      font=("Arial", 30))
                        label_obrigado._set_appearance_mode("dark")
                        label_obrigado.pack(pady=20)

                    if resultado_papel == 0 and resultado_jornal > 0:

                        label_receitas_jornal = ctk.CTkLabel(pagina_folhas_lista, text="Receitas de Jornal",
                                                             font=("Arial", 24))
                        label_receitas_jornal._set_appearance_mode("dark")
                        label_receitas_jornal.pack(pady=40)

                        if resultado_jornal < 3: # Se for menor que 3 ele mostra na pagina a quantidade de botões baseado no resultado_jornal.
                            for i in range(resultado_jornal):
                                lista_botao_receitas_jornal[i](pagina_folhas_lista, janela, menu, menu_func,
                                                               voltar_func).pack(  # Mostra os botões na página.
                                    pady=10)

                        else: # Se não ele mostra na pagina todos os botões
                            for i in range(len(lista_botao_receitas_jornal)):
                                lista_botao_receitas_jornal[i](pagina_folhas_lista, janela, menu, menu_func,
                                                               voltar_func).pack(  # Mostra os botões na página.
                                    pady=10)

                        botao_descarte = ctk.CTkButton(pagina_folhas_lista, text="Descarte", # botao para ir a pagina de descarte caso o usuario nao queira fazer as receitas.
                                                       command=lambda: descarte_lista(pagina_folhas_lista, descarte))
                        botao_descarte._set_appearance_mode("dark")
                        botao_descarte.pack(pady=30)

                    if resultado_papel > 0 and resultado_jornal == 0:

                        label_receitas_papel = ctk.CTkLabel(pagina_folhas_lista, text="Receitas de Papel",
                                                            font=("Arial", 24))
                        label_receitas_papel._set_appearance_mode("dark")
                        label_receitas_papel.pack(pady=50)

                        if resultado_papel < 3: # Se for menor que 3 ele mostra na pagina a quantidade de botões baseado no resultado_papel.
                            for i in range(resultado_papel):
                                lista_botao_receitas_papel[i](pagina_folhas_lista, janela, menu, menu_func, # Mostra os botões na página.
                                                              voltar_func).pack(pady=10)

                        else: # Se não ele mostra na pagina todos os botões
                            for i in range(len(lista_botao_receitas_papel)):
                                lista_botao_receitas_papel[i](pagina_folhas_lista, janela, menu, menu_func,
                                                              voltar_func).pack(  # Mostra os botões na página.
                                    pady=10)


                        botao_descarte = ctk.CTkButton(pagina_folhas_lista, text="Descarte", # botao para ir a pagina de descarte caso o usuario nao queira fazer as receitas.
                                                       command=lambda: descarte_lista(pagina_folhas_lista, descarte))
                        botao_descarte._set_appearance_mode("dark")
                        botao_descarte.pack(pady=30)

                    if resultado_papel > 0 and resultado_jornal > 0: #verifica o valor das duas variaveis.

                        label_receitas_papel = ctk.CTkLabel(pagina_folhas_lista, text="Receitas de Papel", font=("Arial", 24))
                        label_receitas_papel._set_appearance_mode("dark")
                        label_receitas_papel.pack(pady=50)

                        if resultado_papel < 3: # Se for menor que 3 ele mostra na pagina a quantidade de botões baseado no resultado_papel.
                            for i in range(resultado_papel):
                                lista_botao_receitas_papel[i](pagina_folhas_lista, janela, menu, menu_func,
                                                              # Mostra os botões na página.
                                                              voltar_func).pack(pady=10)

                        else: # Se não ele mostra na pagina todos os botões
                            for i in range(len(lista_botao_receitas_papel)):
                                lista_botao_receitas_papel[i](pagina_folhas_lista, janela, menu, menu_func,
                                                              voltar_func).pack(  # Mostra os botões na página.
                                    pady=10)

                        label_receitas_jornal = ctk.CTkLabel(pagina_folhas_lista, text="Receitas de Jornal",
                                                            font=("Arial", 24))
                        label_receitas_jornal._set_appearance_mode("dark")
                        label_receitas_jornal.pack(pady=40)

                        if resultado_jornal < 3: # Se for menor que 3 ele mostra na pagina a quantidade de botões baseado no resultado_jornal.
                            for i in range(resultado_jornal):
                                lista_botao_receitas_jornal[i](pagina_folhas_lista, janela, menu, menu_func, voltar_func).pack( # Mostra os botões na página.
                                    pady=10)

                        else: # Se não ele mostra na pagina todos os botões
                            for i in range(len(lista_botao_receitas_jornal)):
                                lista_botao_receitas_jornal[i](pagina_folhas_lista, janela, menu, menu_func,
                                                               voltar_func).pack(  # Mostra os botões na página.
                                    pady=10)

                        botao_descarte = ctk.CTkButton(pagina_folhas_lista, text="Descarte", # botao para ir a pagina de descarte caso o usuario nao queira fazer as receitas.
                                                       command=lambda: descarte_lista(pagina_folhas_lista, descarte))
                        botao_descarte._set_appearance_mode("dark")
                        botao_descarte.pack(pady=30)

                    label_espaco_papel_lista = ctk.CTkLabel(pagina_folhas_lista,  # Label que cria um espaço na página.
                                                            text="")
                    label_espaco_papel_lista._set_appearance_mode("dark")
                    label_espaco_papel_lista.pack(side="bottom", pady=0)

                    botao_fim = ctk.CTkButton(pagina_folhas_lista, text="Fim", font=("Arial", 24), width=100,
                                              # Botão que avança para a página final.
                                              height=40, fg_color="Red", text_color="White",
                                              command=lambda: fim_receita(pagina_folhas_lista, janela, menu, menu_func,
                                                                          voltar_func))
                    botao_fim._set_appearance_mode("dark")
                    botao_fim.pack(side="bottom", pady=5)

                    botao_result_folhas_menu = ctk.CTkButton(pagina_folhas_lista, text="Menu", font=("Arial", 24), width=100, height=40,  #botao para voltar ao menu inicial dentro da pagina temporaria.
                                                             command=lambda: menu_func(pagina_folhas_lista, menu))
                    botao_result_folhas_menu._set_appearance_mode("dark")
                    botao_result_folhas_menu.pack(side="bottom", pady=5)

                    botao_result_folhas_voltar = ctk.CTkButton(pagina_folhas_lista, text="Voltar", font=("Arial", 24), width=100, height=40,  #botao para voltar a pagina anterior dentro da pagina temporaria.
                                                               command=lambda: voltar_func(pagina_folhas_lista, pagina_sim_jornal))
                    botao_result_folhas_voltar._set_appearance_mode("dark")
                    botao_result_folhas_voltar.pack(side="bottom", pady=5)

            label_menor_entry = ctk.CTkLabel(pagina_sim_jornal, text="Digite a quantidade de folhas de papel A4 que você tem", font=("Arial", 24)) #Texto que pede para digitar a quantidade de papel.
            label_menor_entry._set_appearance_mode("dark")
            label_menor_entry.pack(pady=50)

            """Entrada de dados:"""
            entry_papel = ctk.CTkEntry(pagina_sim_jornal, width=300,
                                       placeholder_text="Digite aqui a quantidade...")
            entry_papel._set_appearance_mode("dark")
            entry_papel.pack()

            label_maior_entry = ctk.CTkLabel(pagina_sim_jornal, text="Digite a quantidade de folhas de jornal que você tem", font=("Arial", 24)) #Texto que pede para digitar a quantidade de jornal.
            label_maior_entry._set_appearance_mode("dark")
            label_maior_entry.pack(pady=50)

            """Entrada de dados:"""
            entry_jornal = ctk.CTkEntry(pagina_sim_jornal, width=300,
                                        placeholder_text="Digite aqui a quantidade...")
            entry_jornal._set_appearance_mode("dark")
            entry_jornal.pack()

            label_certeza_entry = ctk.CTkLabel(pagina_sim_jornal, width=300, text="Tem certeza?", font=("Arial", 24)) #Texto para perguntar se o usuario tem certeza que quer avançar.
            label_certeza_entry._set_appearance_mode("dark")
            label_certeza_entry.pack(pady=20)

            botao_folhas_sim_entry = ctk.CTkButton(pagina_sim_jornal, text="SIM", width=300, command=sim_entry,  #Botão com a opção "SIM" que tem como comando a função sim_entry().
                                                   fg_color="green")
            botao_folhas_sim_entry._set_appearance_mode("dark")
            botao_folhas_sim_entry.pack(pady=10)

            botao_folhas_nao_entry = ctk.CTkButton(pagina_sim_jornal, text="NÃO", width=300, command=nao_entry_plus,  #Botão com a opção "NÃO" que tem como comando a função nao_entry_plus().
                                                   fg_color="red")
            botao_folhas_nao_entry._set_appearance_mode("dark")
            botao_folhas_nao_entry.pack(pady=10)

            label_espaco_sim_maior = ctk.CTkLabel(pagina_sim_jornal,  # Label que cria um espaço na página.
                                                  text="")
            label_espaco_sim_maior._set_appearance_mode("dark")
            label_espaco_sim_maior.pack(side="bottom", pady=0)

            botao_menu2 = ctk.CTkButton(pagina_sim_jornal, text="Menu", font=("Arial", 24), width=100, height=40,  #botao para voltar ao menu inicial dentro da pagina temporaria.
                                        command=lambda: menu_func(pagina_sim_jornal, menu))
            botao_menu2._set_appearance_mode("dark")
            botao_menu2.pack(side= "bottom", pady=5)

            botao_voltar2 = ctk.CTkButton(pagina_sim_jornal, text="Voltar", font=("Arial", 24), width=100, height=40,  #botao para voltar a pagina anterior dentro da pagina temporaria.
                                          command=lambda: voltar_func(pagina_sim_jornal, pagina_sim_papel))
            botao_voltar2._set_appearance_mode("dark")
            botao_voltar2.pack(side= "bottom", pady=5)

        label_espaco = ctk.CTkLabel(pagina_sim_papel, text="",  #label para criar um espaço na pagina.
                                    font=("Arial", 24))
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(pady=170)

        label_maior = ctk.CTkLabel(pagina_sim_papel, text="Você tem alguma quantidade de folha de jornal?",  #texto para fazer a segunda pergunta.
                                   font=("Arial", 24))
        label_maior._set_appearance_mode("dark")
        label_maior.pack(pady=20)
        botao_papel_sim_maior = ctk.CTkButton(pagina_sim_papel, text="SIM", width=200, command=sim_jornal,  #Botão com a opção "SIM" que tem como comando a função sim_maior().
                                              fg_color="green")
        botao_papel_sim_maior._set_appearance_mode("dark")
        botao_papel_sim_maior.pack(pady=10)
        botao_papel_nao_maior = ctk.CTkButton(pagina_sim_papel, text="NÃO", width=200, command=nao_jornal,  #Botão com a opção "NÃO" que tem como comando a função nao_maior().
                                              fg_color="red")
        botao_papel_nao_maior._set_appearance_mode("dark")
        botao_papel_nao_maior.pack(pady=10)

        label_espaco_sim_menor = ctk.CTkLabel(pagina_sim_papel,  # Label que cria um espaço na página.
                                              text="")
        label_espaco_sim_menor._set_appearance_mode("dark")
        label_espaco_sim_menor.pack(side="bottom", pady=0)

        botao_menu = ctk.CTkButton(pagina_sim_papel, text="Menu", font=("Arial", 24), width=100, height=40,  #botao para voltar ao menu inicial dentro da pagina temporaria.
                                   command=lambda: menu_func(pagina_sim_papel, menu))
        botao_menu._set_appearance_mode("dark")
        botao_menu.pack(side="bottom", pady=5)

        botao_voltar = ctk.CTkButton(pagina_sim_papel, text="Voltar", font=("Arial", 24), width=100, height=40,  #botao para voltar a pagina anterior dentro da pagina temporaria.
                                     command=lambda: voltar_func(pagina_sim_papel, pagina_papel_escolha))
        botao_voltar._set_appearance_mode("dark")
        botao_voltar.pack(side="bottom", pady=5)

    label_papel = ctk.CTkLabel(pagina_papel_escolha, text="", font=("Arial", 24)) #label para criar um espaço na pagina.
    label_papel._set_appearance_mode("dark")
    label_papel.pack(pady=170)
    label_pergunta = ctk.CTkLabel(pagina_papel_escolha, width=300, text="Você tem alguma quantidade de papel A4?", font=("Arial", 24)) #texto para fazer a primeira pergunta.
    label_pergunta._set_appearance_mode("dark")
    label_pergunta.pack(pady=20)

    botao_papel_sim = ctk.CTkButton(pagina_papel_escolha, text="SIM", width=200, command= sim_papel, fg_color="green") #Botão com a opção "SIM" que tem como comando a função sim_menor().
    botao_papel_sim._set_appearance_mode("dark")
    botao_papel_sim.pack(pady=10)

    botao_papel_nao = ctk.CTkButton(pagina_papel_escolha, text="NÃO", width=200, command= nao_papel, fg_color="red") #Botão com a opção "SIM" que tem como comando a função nao_menor().
    botao_papel_nao._set_appearance_mode("dark")
    botao_papel_nao.pack(pady=10)

    label_espaco_papel_escolha = ctk.CTkLabel(pagina_papel_escolha,  # Label que cria um espaço na página.
                                              text="")
    label_espaco_papel_escolha._set_appearance_mode("dark")
    label_espaco_papel_escolha.pack(side="bottom", pady=0)

    botao_papel_e_menu = ctk.CTkButton(pagina_papel_escolha, text="Menu", font=("Arial", 24), command=menu, width=100, #Botão para voltar ao menu inicial.
                                       height=40)
    botao_papel_e_menu._set_appearance_mode("dark")
    botao_papel_e_menu.pack(side="bottom", pady=5)

    botao_papel_voltar = ctk.CTkButton(pagina_papel_escolha, text="Voltar", font=("Arial", 24), command=voltar, width=100, height=40) #Botão para voltar à pagina anterior.
    botao_papel_voltar._set_appearance_mode("dark")
    botao_papel_voltar.pack(side= "bottom" ,pady = 5)

    return pagina_papel_escolha #Retorna a pagina da escolha de papel.