import customtkinter as ctk
from tkinter import *
from receitas_papelao import *

lista_botao_receitas_caixa = [botao_receita, botao_receita2]

def nao_entry(entrada): # Função para deletar o que esta escrito dentro da caixa de entrada
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

def pag_papelao_escolha(janela, menu, voltar): #Função da página da escolha "Papelão".

    pagina_papelao_e_ = ctk.CTkFrame(janela) # Cria a página da escolha "Papelão".
    pagina_papelao_e_._set_appearance_mode("dark")

    def nao_menor():  # Função se for escolhida a opção "NÃO" na primeira pergunta.

        pagina_papelao_e_.pack_forget()  # "Esquece" a pagina antiga ou fecha a pagina antiga.
        pagina_nao_menor = ctk.CTkFrame(janela)  # Cria uma nova pagina
        pagina_nao_menor._set_appearance_mode("dark")
        pagina_nao_menor.pack(fill="both", expand=True)

        def sim_entry_n():  # Função se for escolhida a opção "SIM" na pergunta de certeza.

            resultado = entry_maior_n.get()  # Obtem a quantidade inserida no entry e a variavel recebe esse valor.

            """Processamento de dados:"""
            if resultado.isdigit() == False:  # Verifica se o valor da variavel é um digito inteiro.

                label_invalida = ctk.CTkLabel(pagina_nao_menor, # se nao for um digito inteiro este texto aparece na tela.
                                              text="Quantidade Invalida! Digite uma quantidade valida.",
                                              font=("Arial", 24), fg_color="#000000", corner_radius=10, height=40)
                label_invalida._set_appearance_mode("dark")
                label_invalida.pack(pady=50)
                pagina_nao_menor.after(3000, apagar, label_invalida)  # apaga o texto depois de 3 segundos.

            elif resultado.isdigit() == True:  # Verifica se o valor da variavel é um digito inteiro.

                pagina_nao_menor.pack_forget()  # "Esquece" a pagina antiga ou fecha a pagina antiga.

                pagina_papelao_lista_maior = ctk.CTkFrame(janela)  # Cria uma nova pagina
                pagina_papelao_lista_maior._set_appearance_mode("dark")
                pagina_papelao_lista_maior.pack(fill="both", expand=True)

                resultado = int(resultado)  # transforma o valor da variavel em inteiro.

                """Saída de dados:"""
                if resultado == 1:

                    # Receitas se tiver apenas uma quantidade:
                    label2 = ctk.CTkLabel(pagina_papelao_lista_maior,
                                          text="Você consegue fazer apenas esta receita grande:",
                                          font=("Arial", 24))
                    label2._set_appearance_mode("dark")
                    label2.pack(pady=50)
                    label3 = ctk.CTkLabel(pagina_papelao_lista_maior, text="Receita Grande", font=("Arial", 24))
                    label3._set_appearance_mode("dark")
                    label3.pack(pady=20)

                elif resultado == 2:

                    # Receitas se tiver 2 quantidades:
                    label2 = ctk.CTkLabel(pagina_papelao_lista_maior, text="Você consegue fazer estas receitas grandes:",
                                          font=("Arial", 24))
                    label2._set_appearance_mode("dark")
                    label2.pack(pady=50)
                    label3 = ctk.CTkLabel(pagina_papelao_lista_maior, text="Receita Grande 1", font=("Arial", 24))
                    label3._set_appearance_mode("dark")
                    label3.pack(pady=20)
                    label4 = ctk.CTkLabel(pagina_papelao_lista_maior, text="Receita Grande 2", font=("Arial", 24))
                    label4._set_appearance_mode("dark")
                    label4.pack(pady=20)

                label_espaco_result = ctk.CTkLabel(pagina_papelao_lista_maior, text="")  # Label que cria um espaço na página.
                label_espaco_result._set_appearance_mode("dark")
                label_espaco_result.pack(side="bottom", pady=0)

                botao_result_papelao_menu = ctk.CTkButton(pagina_papelao_lista_maior, text="Menu", font=("Arial", 24), # botao para voltar ao menu inicial dentro da pagina temporaria.
                                                          width=100, height=40,
                                                          command=lambda: menu_func(pagina_papelao_lista_maior, menu))
                botao_result_papelao_menu._set_appearance_mode("dark")
                botao_result_papelao_menu.pack(side="bottom", pady=5)

                botao_result_papelao_voltar = ctk.CTkButton(pagina_papelao_lista_maior, text="Voltar", font=("Arial", 24), # botao para voltar a pagina anterior dentro da pagina temporaria.
                                                            width=100, height=40,
                                                            command=lambda: voltar_func(pagina_papelao_lista_maior,
                                                                                     pagina_nao_menor))
                botao_result_papelao_voltar._set_appearance_mode("dark")
                botao_result_papelao_voltar.pack(side="bottom", pady=5)

        label_maior_m = ctk.CTkLabel(pagina_nao_menor,  # Texto que pede para digitar a quantidade de papelão.
                                     text="Digite a quantidade de papelão que você tem maior que 30 cm",
                                     font=("Arial", 24))
        label_maior_m._set_appearance_mode("dark")
        label_maior_m.pack(pady=50)

        """Entrada de dados:"""
        entry_maior_n = ctk.CTkEntry(pagina_nao_menor, width=300,
                                     placeholder_text="Digite aqui a quantidade...")
        entry_maior_n._set_appearance_mode("dark")
        entry_maior_n.pack()

        label_certeza_entry_n = ctk.CTkLabel(pagina_nao_menor, width=300, text="Tem certeza?", # Texto para perguntar se o usuario tem certeza que quer avançar
                                             font=("Arial", 24))
        label_certeza_entry_n._set_appearance_mode("dark")
        label_certeza_entry_n.pack(pady=20)

        botao_papelao_sim_entry_n = ctk.CTkButton(pagina_nao_menor, text="SIM", width=300, command=sim_entry_n, # Botão com a opção "SIM" que tem como comando a função sim_entry_n().
                                                  fg_color="green")
        botao_papelao_sim_entry_n._set_appearance_mode("dark")
        botao_papelao_sim_entry_n.pack(pady=10)
        botao_papelao_nao_entry_n = ctk.CTkButton(pagina_nao_menor, text="NÃO", width=300, # Botão com a opção "NÃO" que tem como comando a função nao_entry().
                                                  command=lambda: nao_entry(entry_maior_n),
                                                  fg_color="red")
        botao_papelao_nao_entry_n._set_appearance_mode("dark")
        botao_papelao_nao_entry_n.pack(pady=10)

        label_espaco2 = ctk.CTkLabel(pagina_nao_menor, text="")  # Label que cria um espaço na página.
        label_espaco2._set_appearance_mode("dark")
        label_espaco2.pack(side="bottom", pady=0)

        botao_menu2 = ctk.CTkButton(pagina_nao_menor, text="Menu", font=("Arial", 24), width=100, height=40,
                                    # botao para voltar ao menu inicial dentro da pagina temporaria.
                                    command=lambda: menu_func(pagina_nao_menor, menu)
                                    )
        botao_menu2._set_appearance_mode("dark")
        botao_menu2.pack(side="bottom", pady=5)

        botao_voltar2 = ctk.CTkButton(pagina_nao_menor, text="Voltar", font=("Arial", 24), width=100, height=40,
                                      # botao para voltar a pagina anterior dentro da pagina temporaria.
                                      command=lambda: voltar_func(pagina_nao_menor, pagina_papelao_e_)
                                      )
        botao_voltar2._set_appearance_mode("dark")
        botao_voltar2.pack(side="bottom", pady=5)

    def sim_menor():  # Função se for escolhida a opção "SIM" na primeira pergunta.

        pagina_papelao_e_.pack_forget()  # "Esquece" a pagina antiga ou fecha a pagina antiga.

        pagina_sim_menor = ctk.CTkFrame(janela)  # Cria uma nova pagina
        pagina_sim_menor._set_appearance_mode("dark")
        pagina_sim_menor.pack(fill="both", expand=True)

        def nao_maior():  # Função se for escolhida a opção "NÃO" na segunda pergunta.

            pagina_sim_menor.pack_forget()  # "Esquece" a pagina antiga ou fecha a pagina antiga.

            pagina_nao_maior = ctk.CTkFrame(janela)  # Cria uma nova pagina
            pagina_nao_maior._set_appearance_mode("dark")
            pagina_nao_maior.pack(fill="both", expand=True)

            def sim_entry():  # Função se for escolhida a opção "SIM" na pergunta de certeza.

                resultado_menor = entry.get()  # Obtem a quantidade inserida no entry e a variavel recebe esse valor.

                """Processamento de dados:"""
                if resultado_menor.isdigit() == False:  # Verifica se o valor da variavel é um digito inteiro.

                    label_invalida = ctk.CTkLabel(pagina_nao_maior, # se nao for um digito inteiro este texto aparece na tela.
                                                  text="Quantidade Invalida! Digite uma quantidade valida.",
                                                  font=("Arial", 24), fg_color="#000000", corner_radius=10, height=40)
                    label_invalida._set_appearance_mode("dark")
                    label_invalida.pack(pady=50)
                    pagina_nao_maior.after(3000, apagar, label_invalida)  # apaga o texto depois de 3 segundos.

                elif resultado_menor.isdigit() == True:  # Verifica se o valor da variavel é um digito inteiro.

                    pagina_nao_maior.pack_forget()  # "Esquece" a pagina antiga ou fecha a pagina antiga.

                    pagina_papelao_lista = ctk.CTkFrame(janela)  # Cria uma nova pagina
                    pagina_papelao_lista._set_appearance_mode("dark")
                    pagina_papelao_lista.pack(fill="both", expand=True)

                    resultado_menor = int(resultado_menor)  # transforma o valor da variavel em inteiro.

                    """Saída de dados:"""
                    if resultado_menor == 1:  # verifica a quantidade.

                        # Receitas se tiver apenas uma quantidade:
                        label2 = ctk.CTkLabel(pagina_papelao_lista,
                                              text="Você consegue fazer apenas esta receita pequena:",
                                              font=("Arial", 24))
                        label2._set_appearance_mode("dark")
                        label2.pack(pady=50)
                        label3 = ctk.CTkLabel(pagina_papelao_lista, text="Receita Pequena", font=("Arial", 24))
                        label3._set_appearance_mode("dark")
                        label3.pack(pady=20)

                    elif resultado_menor == 2:  # verifica a quantidade.

                        # Receitas se tiver 2 quantidades:
                        label2 = ctk.CTkLabel(pagina_papelao_lista, text="Você consegue fazer estas receitas pequenas:",
                                              font=("Arial", 24))
                        label2._set_appearance_mode("dark")
                        label2.pack(pady=50)
                        label3 = ctk.CTkLabel(pagina_papelao_lista, text="Receita Pequena 1", font=("Arial", 24))
                        label3._set_appearance_mode("dark")
                        label3.pack(pady=20)
                        label4 = ctk.CTkLabel(pagina_papelao_lista, text="Receita Pequena 2", font=("Arial", 24))
                        label4._set_appearance_mode("dark")
                        label4.pack(pady=20)

                    label_espaco3 = ctk.CTkLabel(pagina_papelao_lista, text="")  # Label que cria um espaço na página.
                    label_espaco3._set_appearance_mode("dark")
                    label_espaco3.pack(side="bottom", pady=0)

                    botao_result_rolo_menu = ctk.CTkButton(pagina_papelao_lista, text="Menu", font=("Arial", 24), # botao para voltar ao menu inicial dentro da pagina temporaria.
                                                           width=100, height=40,
                                                           command=lambda: menu_func(pagina_papelao_lista, menu))
                    botao_result_rolo_menu._set_appearance_mode("dark")
                    botao_result_rolo_menu.pack(side="bottom", pady=5)

                    botao_result_rolo_voltar = ctk.CTkButton(pagina_papelao_lista, text="Voltar", font=("Arial", 24), # botao para voltar a pagina anterior dentro da pagina temporaria.
                                                             width=100, height=40,
                                                             command=lambda: voltar_func(pagina_papelao_lista,
                                                                                         pagina_nao_maior))
                    botao_result_rolo_voltar._set_appearance_mode("dark")
                    botao_result_rolo_voltar.pack(side="bottom", pady=5)

            label_menor_entry = ctk.CTkLabel(pagina_nao_maior, #Texto que pede para digitar a quantidade de papelão.
                                             text="Digite a quantidade de papelão que você tem menor que 30 cm",
                                             font=("Arial", 24))
            label_menor_entry._set_appearance_mode("dark")
            label_menor_entry.pack(pady=50)

            """Entrada de dados:"""
            entry = ctk.CTkEntry(pagina_nao_maior, width=300,
                                 placeholder_text="Digite aqui a quantidade...")
            entry._set_appearance_mode("dark")
            entry.pack()

            label_certeza_entry = ctk.CTkLabel(pagina_nao_maior, width=300, text="Tem certeza?", # Texto para perguntar se o usuario tem certeza que quer avançar
                                               font=("Arial", 24))
            label_certeza_entry._set_appearance_mode("dark")
            label_certeza_entry.pack(pady=20)

            botao_papelao_sim_entry = ctk.CTkButton(pagina_nao_maior, text="SIM", width=300, command=sim_entry,  # Botão com a opção "SIM" que tem como comando a função sim_entry().
                                                    fg_color="green")
            botao_papelao_sim_entry._set_appearance_mode("dark")
            botao_papelao_sim_entry.pack(pady=10)
            botao_papelao_nao_entry = ctk.CTkButton(pagina_nao_maior, text="NÃO", width=300,  # Botão com a opção "NÃO" que tem como comando a função nao_entry().
                                                    command=lambda: nao_entry(entry),
                                                    fg_color="red")
            botao_papelao_nao_entry._set_appearance_mode("dark")
            botao_papelao_nao_entry.pack(pady=10)

            label_espaco2 = ctk.CTkLabel(pagina_nao_maior, text="")  # Label que cria um espaço na página.
            label_espaco2._set_appearance_mode("dark")
            label_espaco2.pack(side="bottom", pady=0)

            botao_menu2 = ctk.CTkButton(pagina_nao_maior, text="Menu", font=("Arial", 24), width=100, height=40, # botao para voltar ao menu inicial dentro da pagina temporaria.
                                        command=lambda: menu_func(pagina_nao_maior, menu))
            botao_menu2._set_appearance_mode("dark")
            botao_menu2.pack(side="bottom", pady=5)
            botao_voltar2 = ctk.CTkButton(pagina_nao_maior, text="Voltar", font=("Arial", 24), width=100, height=40, # botao para voltar a pagina anterior dentro da pagina temporaria.
                                          command=lambda: voltar_func(pagina_nao_maior, pagina_sim_menor))
            botao_voltar2._set_appearance_mode("dark")
            botao_voltar2.pack(side="bottom", pady=5)

        def sim_maior():  # Função se for escolhida a opção "SIM" na segunda pergunta.

            pagina_sim_menor.pack_forget()  # "Esquece" a pagina antiga ou fecha a pagina antiga.

            pagina_sim_maior = ctk.CTkFrame(janela)  # Cria uma nova pagina
            pagina_sim_maior._set_appearance_mode("dark")
            pagina_sim_maior.pack(fill="both", expand=True)

            def nao_entry_plus():  # Função para deletar o que esta escrito dentro das duas caixas de entrada.
                entry.delete(0, END)
                entry_maior.delete(0, END)

            def sim_entry():  # Função se for escolhida a opção "SIM" na pergunta de certeza.

                resultado_menor = entry.get()  # Obtem a quantidade inserida no primeiro entry e a variavel recebe esse valor.
                resultado_maior = entry_maior.get()  # Obtem a quantidade inserida no segundo entry e a variavel recebe esse valor.

                """Processamento de dados:"""
                if resultado_menor.isdigit() == False:  # Verifica se o valor da primeira variavel é um digito inteiro.

                    label_invalida = ctk.CTkLabel(pagina_sim_maior, # se nao for um digito inteiro este texto aparece na tela.
                                                  text="A Primeira Quantidade está Invalida! Digite uma quantidade valida.",
                                                  font=("Arial", 24), fg_color="#000000", corner_radius=10, height=40)
                    label_invalida._set_appearance_mode("dark")
                    label_invalida.pack(pady=50)
                    pagina_sim_maior.after(3000, apagar, label_invalida)  # apaga o texto depois de 3 segundos.

                if resultado_maior.isdigit() == False:  # Verifica se o valor da segunda variavel é um digito inteiro.

                    label_invalida2 = ctk.CTkLabel(pagina_sim_maior, # se nao for um digito inteiro este texto aparece na tela.
                                                   text="A Segunda Quantidade está Invalida! Digite uma quantidade valida.",
                                                   font=("Arial", 24), fg_color="#000000", corner_radius=10, height=40)

                    label_invalida2._set_appearance_mode("dark")
                    label_invalida2.pack(pady=50)
                    pagina_sim_maior.after(3000, apagar, label_invalida2)  # apaga o texto depois de 3 segundos.

                elif resultado_menor.isdigit() == True and resultado_maior.isdigit() == True:  # Verifica se o valor das duas variaveis é um digito inteiro.

                    pagina_sim_maior.pack_forget()  # "Esquece" a pagina antiga ou fecha a pagina antiga.

                    pagina_papelao_lista = ctk.CTkFrame(janela)  # Cria uma nova pagina
                    pagina_papelao_lista._set_appearance_mode("dark")
                    pagina_papelao_lista.pack(fill="both", expand=True)

                    resultado_menor = int(resultado_menor)  # transforma o valor da variavel em inteiro.
                    resultado_maior = int(resultado_maior)  # transforma o valor da variavel em inteiro.

                    """Saída de dados:"""
                    if resultado_menor == 1 and resultado_maior == 1:  # verifica o valor das duas variaveis.
                        label2 = ctk.CTkLabel(pagina_papelao_lista,
                                              text="Você consegue fazer estas receitas grandes e pequenas:",
                                              font=("Arial", 24))
                        label2._set_appearance_mode("dark")
                        label2.pack(pady=50)
                        label3 = ctk.CTkLabel(pagina_papelao_lista, text="Receita Pequena", font=("Arial", 24))
                        label3._set_appearance_mode("dark")
                        label3.pack(pady=20)
                        label4 = ctk.CTkLabel(pagina_papelao_lista, text="Receita Grande", font=("Arial", 24))
                        label4._set_appearance_mode("dark")
                        label4.pack(pady=20)
                    elif resultado_maior == 1:  # verifica o valor da segunda variavel.
                        label2 = ctk.CTkLabel(pagina_papelao_lista, text="Você consegue fazer apenas uma receita grande",
                                              font=("Arial", 24))
                        label2._set_appearance_mode("dark")
                        label2.pack(pady=50)
                    elif resultado_menor == 2:  # verifica o valor da primeira variavel.
                        label2 = ctk.CTkLabel(pagina_papelao_lista, text="Você consegue fazer estas receitas pequenas:",
                                              font=("Arial", 24))
                        label2._set_appearance_mode("dark")
                        label2.pack(pady=50)
                        label3 = ctk.CTkLabel(pagina_papelao_lista, text="Receita 1", font=("Arial", 24))
                        label3._set_appearance_mode("dark")
                        label3.pack(pady=20)
                        label4 = ctk.CTkLabel(pagina_papelao_lista, text="Receita 2", font=("Arial", 24))
                        label4._set_appearance_mode("dark")
                        label4.pack(pady=20)
                    elif resultado_maior == 2:  # verifica o valor da segunda variavel.
                        label2 = ctk.CTkLabel(pagina_papelao_lista, text="Você consegue fazer estas receitas grandes:",
                                              font=("Arial", 24))
                        label2._set_appearance_mode("dark")
                        label2.pack(pady=50)
                        label3 = ctk.CTkLabel(pagina_papelao_lista, text="Receita 1", font=("Arial", 24))
                        label3._set_appearance_mode("dark")
                        label3.pack(pady=20)
                        label4 = ctk.CTkLabel(pagina_papelao_lista, text="Receita 2", font=("Arial", 24))
                        label4._set_appearance_mode("dark")
                        label4.pack(pady=20)

                    label_espaco2 = ctk.CTkLabel(pagina_papelao_lista, text="")  # Label que cria um espaço na página.
                    label_espaco2._set_appearance_mode("dark")
                    label_espaco2.pack(side="bottom", pady=0)

                    botao_result_rolo_menu = ctk.CTkButton(pagina_papelao_lista, text="Menu", font=("Arial", 24),  # botao para voltar ao menu inicial dentro da pagina temporaria.
                                                           width=100, height=40,
                                                           command=lambda: menu_func(pagina_papelao_lista, menu))
                    botao_result_rolo_menu._set_appearance_mode("dark")
                    botao_result_rolo_menu.pack(side="bottom", pady=5)

                    botao_result_rolo_voltar = ctk.CTkButton(pagina_papelao_lista, text="Voltar", font=("Arial", 24),  # botao para voltar a pagina anterior dentro da pagina temporaria.
                                                             width=100, height=40,
                                                             command=lambda: voltar_func(pagina_papelao_lista,
                                                                                         pagina_sim_maior))
                    botao_result_rolo_voltar._set_appearance_mode("dark")
                    botao_result_rolo_voltar.pack(side="bottom", pady=5)

            label_menor_entry = ctk.CTkLabel(pagina_sim_maior, # Texto que pede para digitar a primeira quantidade de papelão.
                                             text="Digite a quantidade de papelão que você tem menor que 30 cm",
                                             font=("Arial", 24))
            label_menor_entry._set_appearance_mode("dark")
            label_menor_entry.pack(pady=50)

            """Entrada de dados:"""
            entry = ctk.CTkEntry(pagina_sim_maior, width=300,
                                 placeholder_text="Digite aqui a quantidade...")
            entry._set_appearance_mode("dark")
            entry.pack()

            label_maior_entry = ctk.CTkLabel(pagina_sim_maior, # Texto que pede para digitar a segunda quantidade de papelão.
                                             text="Digite a quantidade de papelão que você tem maior que 30 cm",
                                             font=("Arial", 24))
            label_maior_entry._set_appearance_mode("dark")
            label_maior_entry.pack(pady=50)

            """Entrada de dados:"""
            entry_maior = ctk.CTkEntry(pagina_sim_maior, width=300,
                                       placeholder_text="Digite aqui a quantidade...")
            entry_maior._set_appearance_mode("dark")
            entry_maior.pack()

            label_certeza_entry = ctk.CTkLabel(pagina_sim_maior, width=300, text="Tem certeza?", # Texto para perguntar se o usuario tem certeza que quer avançar.
                                               font=("Arial", 24))
            label_certeza_entry._set_appearance_mode("dark")
            label_certeza_entry.pack(pady=20)

            botao_papel_sim_entry = ctk.CTkButton(pagina_sim_maior, text="SIM", width=300, command=sim_entry, # Botão com a opção "SIM" que tem como comando a função sim_entry().
                                                  fg_color="green")
            botao_papel_sim_entry._set_appearance_mode("dark")
            botao_papel_sim_entry.pack(pady=10)
            botao_papel_nao_entry = ctk.CTkButton(pagina_sim_maior, text="NÃO", width=300, command=nao_entry_plus, # Botão com a opção "NÃO" que tem como comando a função nao_entry_plus().
                                                  fg_color="red")
            botao_papel_nao_entry._set_appearance_mode("dark")
            botao_papel_nao_entry.pack(pady=10)

            label_espaco2 = ctk.CTkLabel(pagina_sim_maior, text="")  # Label que cria um espaço na página.
            label_espaco2._set_appearance_mode("dark")
            label_espaco2.pack(side="bottom", pady=0)

            botao_menu2 = ctk.CTkButton(pagina_sim_maior, text="Menu", font=("Arial", 24), width=100, height=40, # botao para voltar ao menu inicial dentro da pagina temporaria.
                                        command=lambda: menu_func(pagina_sim_maior, menu))
            botao_menu2._set_appearance_mode("dark")
            botao_menu2.pack(side="bottom", pady=5)
            botao_voltar2 = ctk.CTkButton(pagina_sim_maior, text="Voltar", font=("Arial", 24), width=100, height=40, # botao para voltar a pagina anterior dentro da pagina temporaria.
                                          command=lambda: voltar_func(pagina_sim_maior, pagina_sim_menor))
            botao_voltar2._set_appearance_mode("dark")
            botao_voltar2.pack(side="bottom", pady=5)

        label_espaco = ctk.CTkLabel(pagina_sim_menor, text="",  # label para criar um espaço na pagina.
                                    font=("Arial", 24))
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(pady=170)

        label_maior = ctk.CTkLabel(pagina_sim_menor, text="Você tem alguma quantidade de papelão maior que 30 cm de area?", # texto para fazer a segunda pergunta.
                                   font=("Arial", 24))
        label_maior._set_appearance_mode("dark")
        label_maior.pack(pady=20)
        botao_papelao_sim_maior = ctk.CTkButton(pagina_sim_menor, text="SIM", width=200, command=sim_maior, # Botão com a opção "SIM" que tem como comando a função sim_maior().
                                                fg_color="green")
        botao_papelao_sim_maior._set_appearance_mode("dark")
        botao_papelao_sim_maior.pack(pady=10)
        botao_papelao_nao_maior = ctk.CTkButton(pagina_sim_menor, text="NÃO", width=200, command=nao_maior, # Botão com a opção "NÃO" que tem como comando a função nao_maior().
                                                fg_color="red")
        botao_papelao_nao_maior._set_appearance_mode("dark")
        botao_papelao_nao_maior.pack(pady=10)

        label_espaco = ctk.CTkLabel(pagina_sim_menor, text="")  # Label que cria um espaço na página.
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(side="bottom", pady=0)

        botao_menu = ctk.CTkButton(pagina_sim_menor, text="Menu", font=("Arial", 24), width=100, height=40, # botao para voltar ao menu inicial dentro da pagina temporaria.
                                   command=lambda: menu_func(pagina_sim_menor, menu))
        botao_menu._set_appearance_mode("dark")
        botao_menu.pack(side="bottom", pady=5)
        botao_voltar = ctk.CTkButton(pagina_sim_menor, text="Voltar", font=("Arial", 24), width=100, height=40, # botao para voltar a pagina anterior dentro da pagina temporaria.
                                     command=lambda: voltar_func(pagina_sim_menor, pagina_papelao_e_))
        botao_voltar._set_appearance_mode("dark")
        botao_voltar.pack(side="bottom", pady=5)

    label_papelao = ctk.CTkLabel(pagina_papelao_e_, text="", font=("Arial", 24))  # label para criar um espaço na pagina.
    label_papelao._set_appearance_mode("dark")
    label_papelao.pack(pady=170)

    label_pergunta = ctk.CTkLabel(pagina_papelao_e_, width=300, # texto para fazer a primeira pergunta.
                                  text="Você tem alguma quantidade de papelão menor que 30 cm de area?",
                                  font=("Arial", 24))
    label_pergunta._set_appearance_mode("dark")
    label_pergunta.pack(pady=20)

    botao_papelao_sim = ctk.CTkButton(pagina_papelao_e_, text="SIM", width=200, command=sim_menor, # Botão com a opção "SIM" que tem como comando a função sim_menor().
                                      fg_color="green")
    botao_papelao_sim._set_appearance_mode("dark")
    botao_papelao_sim.pack(pady=10)
    botao_papelao_nao = ctk.CTkButton(pagina_papelao_e_, text="NÃO", width=200, command=nao_menor, # Botão com a opção "SIM" que tem como comando a função nao_menor().
                                      fg_color="red")
    botao_papelao_nao._set_appearance_mode("dark")
    botao_papelao_nao.pack(pady=10)

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

def pag_caixa(janela, menu, voltar): #função da página da escolha "Caixa".

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
            if resultado > 0:  # verifica o valor da variavel.

                # Receitas se tiver apenas uma quantidade:

                for i in range(resultado):
                    lista_botao_receitas_caixa[i](pagina_lista_caixa, janela, menu, menu_func, voltar_func).pack(pady=10)

            label_espaco = ctk.CTkLabel(pagina_lista_caixa, text="")  # Label que cria um espaço na página.
            label_espaco._set_appearance_mode("dark")
            label_espaco.pack(side="bottom", pady=0)

            botao_result_caixa_menu = ctk.CTkButton(pagina_lista_caixa, text="Menu", font=("Arial", 24), width=100, # botao para voltar ao menu inicial dentro da pagina temporaria.
                                                    height=40,
                                                    command=lambda: menu_func(pagina_lista_caixa, menu))
            botao_result_caixa_menu._set_appearance_mode("dark")
            botao_result_caixa_menu.pack(side="bottom", pady=5)

            botao_result_caixa_voltar = ctk.CTkButton(pagina_lista_caixa, text="Voltar", font=("Arial", 24), width=100, # botao para voltar a pagina anterior dentro da pagina temporaria.
                                                      height=40, command=lambda: voltar_func(pagina_lista_caixa, pagina_caixa))
            botao_result_caixa_voltar._set_appearance_mode("dark")
            botao_result_caixa_voltar.pack(side="bottom", pady=5)

    label_rolo = ctk.CTkLabel(pagina_caixa, text="Caixa de Papelão", # Cria o texto da pagina da Caixa de Papelão: "Caixa de Papelão".
                              font=("Arial", 24))
    label_rolo._set_appearance_mode("dark")
    label_rolo.pack(pady=50)

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