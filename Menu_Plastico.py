import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
from receitas_plastico import *

def descarte_lista(pag_atual, descarte):
    pag_atual.pack_forget()
    descarte()

lista_botao_receitas_garrafa = [botao_receita, botao_receita2, botao_receita3]

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


def pag_garrafa_PET(janela, menu, voltar, descarte): # Função da página da garrafa PET

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

            pagina = ctk.CTkFrame(janela)  # Cria uma nova pagina
            pagina._set_appearance_mode("dark")
            pagina.pack(fill="both", expand=True)

            label_receitas = ctk.CTkLabel(pagina, text="Receitas", font=("Arial", 24))
            label_receitas._set_appearance_mode("dark")
            label_receitas.pack(pady=50)

            resultado = int(resultado)  # transforma o valor da variavel em inteiro.

            """Saída de dados:"""

            if resultado == 0:

                # Texto se o resultado for 0

                label_triste = ctk.CTkLabel(pagina, text=":(", font=("Arial", 40))
                label_triste._set_appearance_mode("dark")
                label_triste.pack(pady=20)

                label_juntar = ctk.CTkLabel(pagina, text="Junte mais garrafas PET", font=("Arial", 30))
                label_juntar._set_appearance_mode("dark")
                label_juntar.pack(pady=20)

                label_juntar2 = ctk.CTkLabel(pagina,
                                             text="ou pegue mais com vizinhos/amigos/familiares.",
                                             font=("Arial", 30))
                label_juntar2._set_appearance_mode("dark")
                label_juntar2.pack(pady=20)

                label_obrigado = ctk.CTkLabel(pagina,
                                              text="Agradeçemos por usar o nosso programa, Volte novamente!",
                                              font=("Arial", 30))
                label_obrigado._set_appearance_mode("dark")
                label_obrigado.pack(pady=20)

            if resultado == 1:  # verifica o valor da variavel.

                # Receitas se tiver apenas uma quantidade:

                lista_botao_receitas_garrafa[0](pagina, janela, menu, menu_func, voltar_func).pack(pady=10)

                botao_descarte = ctk.CTkButton(pagina, text="Descarte",
                                               # botao para ir a pagina de descarte caso o usuario nao queira fazer as receitas.
                                               command=lambda: descarte_lista(pagina, descarte))
                botao_descarte._set_appearance_mode("dark")
                botao_descarte.pack(pady=10)

            if 1 < resultado < 5:  # verifica o valor da variavel.

                # Receitas se tiver mais que uma quantidade e menos que cinco:
                for i in range(2):
                    lista_botao_receitas_garrafa[i](pagina, janela, menu, menu_func, voltar_func).pack(pady=10)

                botao_descarte = ctk.CTkButton(pagina, text="Descarte",
                                               # botao para ir a pagina de descarte caso o usuario nao queira fazer as receitas.
                                               command=lambda: descarte_lista(pagina, descarte))
                botao_descarte._set_appearance_mode("dark")
                botao_descarte.pack(pady=10)

            if resultado >= 5:  # verifica o valor da variavel.

                # Receitas se tiver cinco ou mais quantidades:
                for i in range(len(lista_botao_receitas_garrafa)):
                    lista_botao_receitas_garrafa[i](pagina, janela, menu, menu_func, voltar_func).pack(pady=10)

                botao_descarte = ctk.CTkButton(pagina, text="Descarte",
                                               # botao para ir a pagina de descarte caso o usuario nao queira fazer as receitas.
                                               command=lambda: descarte_lista(pagina, descarte))
                botao_descarte._set_appearance_mode("dark")
                botao_descarte.pack(pady=10)

            label_espaco = ctk.CTkLabel(pagina, text="")  # Label que cria um espaço na página.
            label_espaco._set_appearance_mode("dark")
            label_espaco.pack(side="bottom", pady=0)

            botao_fim = ctk.CTkButton(pagina, text="Fim", font=("Arial", 24), width=100, # Botão que avança para a página final.
                                      height=40, fg_color="Red", text_color="White",
                                      command=lambda: fim_receita(pagina, janela, menu, menu_func, voltar_func))
            botao_fim._set_appearance_mode("dark")
            botao_fim.pack(side="bottom", pady=5)

            botao_result_jornal_menu = ctk.CTkButton(pagina, text="Menu", font=("Arial", 24), width=100,  # botao para voltar ao menu inicial dentro da pagina temporaria.
                                                     height=40,
                                                     command=lambda: menu_func(pagina, menu))
            botao_result_jornal_menu._set_appearance_mode("dark")
            botao_result_jornal_menu.pack(side="bottom", pady=5)

            botao_result_jornal_voltar = ctk.CTkButton(pagina, text="Voltar", font=("Arial", 24),  # botao para voltar a pagina anterior dentro da pagina temporaria.
                                                       width=100, height=40,
                                                       command=lambda: voltar_func(pagina, pagina_garrafa_pet))
            botao_result_jornal_voltar._set_appearance_mode("dark")
            botao_result_jornal_voltar.pack(side="bottom", pady=5)

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

    label_espaco1 = ctk.CTkLabel(pagina_garrafa_pet, text="")  # Label que cria um espaço na página.
    label_espaco1._set_appearance_mode("dark")
    label_espaco1.pack(side="bottom", pady=0)

    botao_garrafas_menu = ctk.CTkButton(pagina_garrafa_pet, text="Menu", font=("Arial", 24), width=100, height=40, # Botão para voltar ao menu inicial.
                                        command=menu)
    botao_garrafas_menu._set_appearance_mode("dark")
    botao_garrafas_menu.pack(side="bottom", pady=5)

    botao_garrafas_voltar = ctk.CTkButton(pagina_garrafa_pet, text="Voltar", font=("Arial", 24), width=100, # Botão para voltar à pagina anterior.
                                          height=40, command=voltar)
    botao_garrafas_voltar._set_appearance_mode("dark")
    botao_garrafas_voltar.pack(side="bottom", pady=5)
    return pagina_garrafa_pet


def pag_tampa(janela, menu, voltar):
    pagina_tampa = ctk.CTkFrame(janela) # Cria a página da tampa
    pagina_tampa._set_appearance_mode("dark")

    def nao():
        pagina_tampa.pack_forget() # "Esquece" ou fecha a página passada.

        pagina_tampa_nao = ctk.CTkFrame(janela) # Cria uma nova página.
        pagina_tampa_nao._set_appearance_mode("dark")
        pagina_tampa_nao.pack(fill="both", expand=True)

        label_espaco = ctk.CTkLabel(pagina_tampa_nao, text="")  # Label que cria um espaço na página.
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(pady=50)

        # Texto caso a pessoa não tenha tampas.

        label_triste = ctk.CTkLabel(pagina_tampa_nao, text=":(", font=("Arial", 40))
        label_triste._set_appearance_mode("dark")
        label_triste.pack(pady=20)

        label_juntar = ctk.CTkLabel(pagina_tampa_nao, text="Junte mais tampas", font=("Arial", 30))
        label_juntar._set_appearance_mode("dark")
        label_juntar.pack(pady=20)

        label_juntar2 = ctk.CTkLabel(pagina_tampa_nao, text="ou pegue mais tampas com vizinhos/amigos/familiares.",
                                     font=("Arial", 30))
        label_juntar2._set_appearance_mode("dark")
        label_juntar2.pack(pady=20)

        label_obrigado = ctk.CTkLabel(pagina_tampa_nao, text="Agradeçemos por usar o nosso programa, Volte novamente!",
                                      font=("Arial", 30))
        label_obrigado._set_appearance_mode("dark")
        label_obrigado.pack(pady=20)

        label_espaco2 = ctk.CTkLabel(pagina_tampa_nao, text="") # Label que cria um espaço na pagina.
        label_espaco2._set_appearance_mode("dark")
        label_espaco2.pack(side="bottom", pady=0)

        botao_fechar = ctk.CTkButton(pagina_tampa_nao, text="FECHAR", font=("Arial", 24), width=100, # Botão que finaliza o programa.
                                     height=40, text_color="White", fg_color="Red",
                                     command=fechar)
        botao_fechar._set_appearance_mode("dark")
        botao_fechar.pack(side="bottom", pady=5)

        botao_tampa_nao_menu = ctk.CTkButton(pagina_tampa_nao, text="Menu", font=("Arial", 30), width=100, # Botão que volta ao menu inicial dentro da pagina temporária.
                                             height=40,
                                             command=lambda: menu_func(pagina_tampa_nao, menu))
        botao_tampa_nao_menu._set_appearance_mode("dark")
        botao_tampa_nao_menu.pack(side="bottom", pady=5)

        botao_tampa_nao_voltar = ctk.CTkButton(pagina_tampa_nao, text="Voltar", font=("Arial", 30), width=100, # Botão que volta a página anterior dentro da pagina temporária.
                                               height=40,
                                               command=lambda: voltar_func(pagina_tampa_nao, pagina_tampa))
        botao_tampa_nao_voltar._set_appearance_mode("dark")
        botao_tampa_nao_voltar.pack(side="bottom", pady=5)

    def sim():
        pagina_tampa.pack_forget() # "Esquece" ou fecha a página passada.

        pagina_tampa_sim = ctk.CTkFrame(janela) # Cria uma nova página.
        pagina_tampa_sim._set_appearance_mode("dark")
        pagina_tampa_sim.pack(fill="both", expand=True)

        label_receita_tampa = ctk.CTkLabel(pagina_tampa_sim, # Label com o Titulo da receita
                                           text="Cobras com tampas de plástico", font=("Arial", 24))
        label_receita_tampa._set_appearance_mode("dark")
        label_receita_tampa.pack(pady=20)

        label_materiais = ctk.CTkLabel(pagina_tampa_sim, # Label com os Materiais da receita
                                       text="Materiais: Tampas de garrafas de plástico (se forem de várias cores, melhor), 2 tampas de plástico maiores (talvez de algum produto de limpeza), Chave de fenda, Barbante e Marcador."
                                       , font=("Arial", 20))

        label_materiais._set_appearance_mode("dark")
        label_materiais.pack(pady=20)

        imagem1 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_tampas.png"), size=(300, 200)) # Alocação de uma imagem para uma variavel.

        label_imagem1 = ctk.CTkLabel(pagina_tampa_sim, image=imagem1, text="")
        label_imagem1.pack(pady=0) # Coloca a imagem na página

        abas = ctk.CTkTabview(pagina_tampa_sim, height=150, segmented_button_fg_color="White", segmented_button_unselected_color="#A7C7E7", segmented_button_unselected_hover_color="#A7C7E7", segmented_button_selected_color="#B0E0E6", text_color="Black") # Cria a aba
        abas._set_appearance_mode("dark")
        abas.pack()
        abas.add("Passo 1") # Adiciona seções na aba
        abas.add("Passo 2")
        abas.add("Passo 3")
        abas.add("Passo 4")

        label_passo1 = ctk.CTkLabel(abas.tab("Passo 1"), # Label do primeiro passo.
                                    text="1. Faça pequenos orifícios no centro de cada tampa com a chave de fenda."
                                    , font=("Arial", 22))
        label_passo1._set_appearance_mode("dark")
        label_passo1.pack(pady=20)

        label_passo2 = ctk.CTkLabel(abas.tab("Passo 2"), # Label do segundo passo.
                                    text="2. Pegue o barbante e dê um nó."
                                    , font=("Arial", 22))
        label_passo2._set_appearance_mode("dark")
        label_passo2.pack(pady=20)

        label_passo3 = ctk.CTkLabel(abas.tab("Passo 3"), # Label do terceiro passo.
                                    text="3. Insira a tampa de plástico que seria a cabeça e continue acrescentando cada tampa do corpo da cobra pelo barbante."
                                    , font=("Arial", 22))
        label_passo3._set_appearance_mode("dark")
        label_passo3.pack(pady=20)

        label_passo4 = ctk.CTkLabel(abas.tab("Passo 4"), # Label do quarto passo.
                                    text="4. Não se esqueça de inserir a cauda por último."
                                    , font=("Arial", 22))
        label_passo4._set_appearance_mode("dark")
        label_passo4.pack(pady=20)

        label_espaco = ctk.CTkLabel(pagina_tampa_sim, text="") # Label que cria um espaço na página.
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(side="bottom", pady=0)

        botao_fim = ctk.CTkButton(pagina_tampa_sim, text="Fim", font=("Arial", 24), width=100, # Botão que avança para a página final.
                                  height=40, fg_color="Red", text_color="White",
                                  command=lambda: fim_receita(pagina_tampa_sim, janela, menu, menu_func, voltar_func))
        botao_fim._set_appearance_mode("dark")
        botao_fim.pack(side="bottom", pady=5)

        botao_tampa_receita_menu = ctk.CTkButton(pagina_tampa_sim, text="Menu", font=("Arial", 24), width=100, # Botão que volta ao menu inicial dentro da pagina temporária.
                                                 height=40,
                                                 command=lambda: menu_func(pagina_tampa_sim, menu))
        botao_tampa_receita_menu._set_appearance_mode("dark")
        botao_tampa_receita_menu.pack(side="bottom", pady=5)

        botao_tampa_receita_voltar = ctk.CTkButton(pagina_tampa_sim, text="Voltar", font=("Arial", 24), width=100, # Botão que volta a página anterior dentro da pagina temporária.
                                                   height=40,
                                                   command=lambda: voltar_func(pagina_tampa_sim, pagina_tampa))
        botao_tampa_receita_voltar._set_appearance_mode("dark")
        botao_tampa_receita_voltar.pack(side="bottom", pady=5)

    label_tampa = ctk.CTkLabel(pagina_tampa, text="", font=("Arial", 24)) # Label que cria um espaço na página
    label_tampa._set_appearance_mode("dark")
    label_tampa.pack(pady=170)

    label_pergunta = ctk.CTkLabel(pagina_tampa, width=300, # Label para fazer a pergunta.
                                  text="Você tem pelo menos duas tampas de garrafa de plástico?",
                                  font=("Arial", 24))
    label_pergunta._set_appearance_mode("dark")
    label_pergunta.pack(pady=20)

    botao_tampa_sim = ctk.CTkButton(pagina_tampa, text="SIM", width=200, command=sim, # Botão com a opção "SIM" que tem como comando a função sim().
                                    fg_color="green")
    botao_tampa_sim._set_appearance_mode("dark")
    botao_tampa_sim.pack(pady=10)
    botao_tampa_nao = ctk.CTkButton(pagina_tampa, text="NÃO", width=200, command=nao, # Botão com a opção "SIM" que tem como comando a função nao().
                                    fg_color="red")
    botao_tampa_nao._set_appearance_mode("dark")
    botao_tampa_nao.pack(pady=10)

    label_espaco = ctk.CTkLabel(pagina_tampa, text="") # Label que cria um espaço na página
    label_espaco._set_appearance_mode("dark")
    label_espaco.pack(side="bottom", pady=0)

    botao_tampa_menu = ctk.CTkButton(pagina_tampa, text="Menu", font=("Arial", 24), width=100, height=40, # Botão que retorna ao menu inicial.
                                     command=menu)
    botao_tampa_menu._set_appearance_mode("dark")
    botao_tampa_menu.pack(side="bottom", pady=5)

    botao_tampa_voltar = ctk.CTkButton(pagina_tampa, text="Voltar", font=("Arial", 24), width=100, # Botão que retorna a página anterior.
                                       height=40,
                                       command=voltar)
    botao_tampa_voltar._set_appearance_mode("dark")
    botao_tampa_voltar.pack(side="bottom", pady=5)

    return pagina_tampa # Retorna a pagina da tampa.