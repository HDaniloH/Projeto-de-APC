import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
from receitas_plastico import *


"""def botao_receita(pagina, janela, menu): # função do botão da receita.

    def receita(): # função da pagina da receita.

        pagina.pack_forget() # "Esquece" a página anterior ou fecha a página anterior.

        frame_receita_garrafa_pet = ctk.CTkFrame(janela) # Cria uma nova página.
        frame_receita_garrafa_pet._set_appearance_mode("dark")
        frame_receita_garrafa_pet.pack(fill="both", expand=True)

        label_receita_garrafa_pet = ctk.CTkLabel(frame_receita_garrafa_pet, # Label que fala a receita.
                                                 text="Materiais: Garrafa pet, tinta, tesoura ou estilete, caneta para marcação", font= ("Arial", 25))
        label_receita_garrafa_pet._set_appearance_mode("dark")
        label_receita_garrafa_pet.pack(pady=20)

        imagem1 = ctk.CTkImage(light_image=Image.open("Vasinhos de Plantas com Garrafa Pet 1.jpeg"), size=(300, 200))
        imagem2 = ctk.CTkImage(light_image=Image.open("Vasinhos de Plantas com Garrafa Pet 2.jpeg"), size=(300, 200))
        imagem3 = ctk.CTkImage(light_image=Image.open("Vasinhos de Plantas com Garrafa Pet 3.jpeg"), size=(300, 200))
        imagem4 = ctk.CTkImage(light_image=Image.open("Vasinhos de Plantas com Garrafa Pet 4.jpeg"), size=(300, 200))
        imagem5 = ctk.CTkImage(light_image=Image.open("Vasinhos de Plantas com Garrafa Pet 5.jpeg"), size=(300, 200))

        abas = ctk.CTkTabview(frame_receita_garrafa_pet, segmented_button_fg_color="White", segmented_button_unselected_color="#A7C7E7", segmented_button_unselected_hover_color="#A7C7E7", segmented_button_selected_color="#B0E0E6", text_color="Black")
        abas._set_appearance_mode("dark")
        abas.pack(pady=20)

        abas.add("Passo 1")
        abas.add("Passo 2")
        abas.add("Passo 3")
        abas.add("Passo 4")
        abas.add("Passo 5")

        label_passo1 = ctk.CTkLabel(abas.tab("Passo 1"), # Label com o primeiro passo.
                                    text="1. Marque na garrafa pet o formato que queira o vaso.", font=("Arial", 22))
        label_passo1._set_appearance_mode("dark")
        label_passo1.pack(pady=20)
        label_imagem1 = ctk.CTkLabel(abas.tab("Passo 1"), image=imagem1, text="") #Imagem do primeiro passo.
        label_imagem1.pack(pady=0)

        label_passo2 = ctk.CTkLabel(abas.tab("Passo 2"), # Label com o segundo passo.
                                    text="2. Recorte a garrafa seguindo a marcação.", font=("Arial", 22))
        label_passo2._set_appearance_mode("dark")
        label_passo2.pack(pady=20)
        label_imagem2 = ctk.CTkLabel(abas.tab("Passo 2"), image=imagem2, text="") # Imagem do segundo passo.
        label_imagem2.pack(pady=0)

        label_passo3 = ctk.CTkLabel(abas.tab("Passo 3"), # Label com o terceiro passo.
                                    text="3. Fure o fundo da garrafa para que a água possa escorrer.", font=("Arial", 22))
        label_passo3._set_appearance_mode("dark")
        label_passo3.pack(pady=20)
        label_imagem3 = ctk.CTkLabel(abas.tab("Passo 3"), image=imagem3, text="") # Imagem do terceiro passo.
        label_imagem3.pack(pady=0)

        label_passo4 = ctk.CTkLabel(abas.tab("Passo 4"), # Label com o quarto passo.
                                    text="4. Pinte e decore o vaso como preferir.", font=("Arial", 22))
        label_passo4._set_appearance_mode("dark")
        label_passo4.pack(pady=20)
        label_imagem4 = ctk.CTkLabel(abas.tab("Passo 4"), image=imagem4, text="") # Imagem do quarto passo.
        label_imagem4.pack(pady=0)

        label_passo5 = ctk.CTkLabel(abas.tab("Passo 5"), # Label com o quinto passo.
                                    text="5. Após pintar e decorar a garrafa, plante a semente ou muda que quiser!!", font=("Arial", 22))
        label_passo5._set_appearance_mode("dark")
        label_passo5.pack(pady=20)
        label_imagem5 = ctk.CTkLabel(abas.tab("Passo 5"), image=imagem5, text="") # Imagem do quinto passo.
        label_imagem5.pack(pady=0)

        label_espaco = ctk.CTkLabel(frame_receita_garrafa_pet, text="") # Label que cria um espaço na página.
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(side="bottom", pady=0)

        botao_receita_menu = ctk.CTkButton(frame_receita_garrafa_pet, text="Menu", font=("Arial", 24), width=100, # Botão que volta ao menu inicial dentro da página temporária.
                                           height=40,
                                           command=lambda: menu_func(frame_receita_garrafa_pet, menu))
        botao_receita_menu._set_appearance_mode("dark")
        botao_receita_menu.pack(side="bottom", pady=5)

        botao_receita_voltar = ctk.CTkButton(frame_receita_garrafa_pet, text="Voltar", font=("Arial", 24), width=100, # Botão que volta á pagina anterior dentro da página temporária.
                                             height=40,
                                             command=lambda: voltar_func(frame_receita_garrafa_pet, pagina))
        botao_receita_voltar._set_appearance_mode("dark")
        botao_receita_voltar.pack(side="bottom", pady=5)

    botao_receita = ctk.CTkButton(pagina, text="Vasinhos de Plantas com Garrafa Pet", command=receita, # Botão com o nome da receita que tem como comando a função receita().
                                  fg_color="#A7C7E7", text_color="black", hover_color="#B0E0E6")
    botao_receita._set_appearance_mode("dark")

    return botao_receita # retorna o botão da receita.


def botao_receita2(pagina, janela, menu): # função do botão da receita 2.

    def receita(): # função da pagina da receita 2.

        pagina.pack_forget() # "Esquece" a página anterior ou fecha a página anterior.

        frame_receita_garrafa_pet = ctk.CTkFrame(janela) # Cria uma nova página.
        frame_receita_garrafa_pet._set_appearance_mode("dark")
        frame_receita_garrafa_pet.pack(fill="both", expand=True)

        label_receita_garrafa_pet = ctk.CTkLabel(frame_receita_garrafa_pet, text="Materiais: Duas garrafas grandes de plástico, dois pratos, um estilete, silicone e um marcador.", font= ("Arial", 25))
        label_receita_garrafa_pet._set_appearance_mode("dark")
        label_receita_garrafa_pet.pack(pady=20)

        imagem1 = ctk.CTkImage(light_image=Image.open("repositor de racao.png"), size=(200, 100))
        label_imagem1 = ctk.CTkLabel(frame_receita_garrafa_pet, image=imagem1, text="")  # Imagem do primeiro passo.
        label_imagem1.pack(pady=0)

        abas = ctk.CTkTabview(frame_receita_garrafa_pet, width=1000, height=600)
        abas._set_appearance_mode("dark")
        abas.pack(pady=20)

        abas.add("Passo 1")
        abas.add("Passo 2")
        abas.add("Passo 3")
        abas.add("Passo 4")
        abas.add("Passo 5")

        label_passo1 = ctk.CTkLabel(abas.tab("Passo 1"), # Label com o primeiro passo.
                                    text="1. Exemplo.")
        label_passo1._set_appearance_mode("dark")
        label_passo1.pack(pady=20)

        label_passo2 = ctk.CTkLabel(abas.tab("Passo 2"),  # Label com o primeiro passo.
                                    text="2. Exemplo.")
        label_passo2._set_appearance_mode("dark")
        label_passo2.pack(pady=20)

        label_passo3 = ctk.CTkLabel(abas.tab("Passo 3"),  # Label com o primeiro passo.
                                    text="3. Exemplo.")
        label_passo3._set_appearance_mode("dark")
        label_passo3.pack(pady=20)

        label_passo4 = ctk.CTkLabel(abas.tab("Passo 4"),  # Label com o primeiro passo.
                                    text="4. Exemplo.")
        label_passo4._set_appearance_mode("dark")
        label_passo4.pack(pady=20)

        label_passo5 = ctk.CTkLabel(abas.tab("Passo 5"),  # Label com o primeiro passo.
                                    text="5. Exemplo.")
        label_passo5._set_appearance_mode("dark")
        label_passo5.pack(pady=20)


        label_espaco = ctk.CTkLabel(frame_receita_garrafa_pet, text="")
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(side="bottom", pady=10)

        botao_receita_menu = ctk.CTkButton(frame_receita_garrafa_pet, text="Menu", font=("Arial", 24), width=100,
                                           height=40,
                                           command=lambda: menu_func(frame_receita_garrafa_pet, menu))
        botao_receita_menu._set_appearance_mode("dark")
        botao_receita_menu.pack(side="bottom", pady=10)

        botao_receita_voltar = ctk.CTkButton(frame_receita_garrafa_pet, text="Voltar", font=("Arial", 24), width=100,
                                             height=40,
                                             command=lambda: voltar_func(frame_receita_garrafa_pet, pagina))
        botao_receita_voltar._set_appearance_mode("dark")
        botao_receita_voltar.pack(side="bottom", pady=0)

    botao_receita2 = ctk.CTkButton(pagina, text="Receita Tal", command=receita, fg_color="#A7C7E7", text_color="black",
                                   hover_color="#B0E0E6")
    botao_receita2._set_appearance_mode("dark")
    return botao_receita2"""

lista_botao_receitas_garrafa = [botao_receita, botao_receita2]

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

            pagina = ctk.CTkFrame(janela)  # Cria uma nova pagina
            pagina._set_appearance_mode("dark")
            pagina.pack(fill="both", expand=True)

            label_receitas = ctk.CTkLabel(pagina, text="Receitas", font=("Arial", 24))
            label_receitas._set_appearance_mode("dark")
            label_receitas.pack(pady=50)

            resultado = int(resultado)  # transforma o valor da variavel em inteiro.

            """Saída de dados:"""
            if resultado > 0:  # verifica o valor da variavel.

                # Receitas se tiver apenas uma quantidade:

                for i in range(resultado):
                    lista_botao_receitas_garrafa[i](pagina, janela, menu, menu_func, voltar_func).pack(pady=10)

            label_espaco = ctk.CTkLabel(pagina, text="")  # Label que cria um espaço na página.
            label_espaco._set_appearance_mode("dark")
            label_espaco.pack(side="bottom", pady=0)

            botao_result_jornal_menu = ctk.CTkButton(pagina, text="Menu", font=("Arial", 24), width=100,  # botao para voltar ao menu inicial dentro da pagina temporaria.
                                                     height=40,
                                                     command=lambda: menu_func(pagina, menu))
            botao_result_jornal_menu._set_appearance_mode("dark")
            botao_result_jornal_menu.pack(side="bottom", pady=5)

            botao_result_jornal_voltar = ctk.CTkButton(pagina, text="Voltar", font=("Arial", 24),  # botao para voltar a pagina anterior dentro da pagina temporaria.
                                                       width=100, height=40,
                                                       command=lambda: voltar_func(pagina,
                                                                                   pagina_garrafa_pet))
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
    pagina_tampa = ctk.CTkFrame(janela)
    pagina_tampa._set_appearance_mode("dark")

    def nao():
        pagina_tampa.pack_forget()

        pagina_tampa_nao = ctk.CTkFrame(janela)
        pagina_tampa_nao._set_appearance_mode("dark")
        pagina_tampa_nao.pack(fill="both", expand=True)

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

        label_espaco = ctk.CTkLabel(pagina_tampa_nao, text="")
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(side="bottom", pady=0)

        botao_tampa_nao_menu = ctk.CTkButton(pagina_tampa_nao, text="Menu", font=("Arial", 30), width=100,
                                             height=40,
                                             command=lambda: menu_func(pagina_tampa_nao, menu))
        botao_tampa_nao_menu._set_appearance_mode("dark")
        botao_tampa_nao_menu.pack(side="bottom", pady=5)

        botao_tampa_nao_voltar = ctk.CTkButton(pagina_tampa_nao, text="Voltar", font=("Arial", 30), width=100,
                                               height=40,
                                               command=lambda: voltar_func(pagina_tampa_nao, pagina_tampa))
        botao_tampa_nao_voltar._set_appearance_mode("dark")
        botao_tampa_nao_voltar.pack(side="bottom", pady=5)

    def sim():
        pagina_tampa.pack_forget()
        pagina_tampa_sim = ctk.CTkFrame(janela)
        pagina_tampa_sim._set_appearance_mode("dark")
        pagina_tampa_sim.pack(fill="both", expand=True)

        label_receita_tampa = ctk.CTkLabel(pagina_tampa_sim,
                                           text="Cobras com tampas de plástico", font=("Arial", 24))
        label_receita_tampa._set_appearance_mode("dark")
        label_receita_tampa.pack(pady=20)

        label_materiais = ctk.CTkLabel(pagina_tampa_sim,
                                       text="Materiais: Tampas de garrafas de plástico (se forem de várias cores, melhor), 2 tampas de plástico maiores (talvez de algum produto de limpeza), Chave de fenda, Barbante e Marcador."
                                       , font=("Arial", 20))

        label_materiais._set_appearance_mode("dark")
        label_materiais.pack(pady=20)

        imagem1 = ctk.CTkImage(light_image=Image.open("passo_tampas.png"), size=(300, 200))
        label_imagem1 = ctk.CTkLabel(pagina_tampa_sim, image=imagem1, text="")
        label_imagem1.pack(pady=0)

        abas = ctk.CTkTabview(pagina_tampa_sim, height=150, segmented_button_fg_color="White", segmented_button_unselected_color="#A7C7E7", segmented_button_unselected_hover_color="#A7C7E7", segmented_button_selected_color="#B0E0E6", text_color="Black")
        abas._set_appearance_mode("dark")
        abas.pack()
        abas.add("Passo 1")
        abas.add("Passo 2")
        abas.add("Passo 3")
        abas.add("Passo 4")

        label_passo1 = ctk.CTkLabel(abas.tab("Passo 1"),
                                    text="1. Faça pequenos orifícios no centro de cada tampa com a chave de fenda."
                                    , font=("Arial", 22))
        label_passo1._set_appearance_mode("dark")
        label_passo1.pack(pady=20)

        label_passo2 = ctk.CTkLabel(abas.tab("Passo 2"),
                                    text="2. Pegue o barbante e dê um nó."
                                    , font=("Arial", 22))
        label_passo2._set_appearance_mode("dark")
        label_passo2.pack(pady=20)

        label_passo3 = ctk.CTkLabel(abas.tab("Passo 3"),
                                    text="3. Insira a tampa de plástico que seria a cabeça e continue acrescentando cada tampa do corpo da cobra pelo barbante."
                                    , font=("Arial", 22))
        label_passo3._set_appearance_mode("dark")
        label_passo3.pack(pady=20)

        label_passo4 = ctk.CTkLabel(abas.tab("Passo 4"),
                                    text="4. Não se esqueça de inserir a cauda por último."
                                    , font=("Arial", 22))
        label_passo4._set_appearance_mode("dark")
        label_passo4.pack(pady=20)

        label_espaco = ctk.CTkLabel(pagina_tampa_sim, text="")
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(side="bottom", pady=0)

        botao_tampa_receita_menu = ctk.CTkButton(pagina_tampa_sim, text="Menu", font=("Arial", 24), width=100,
                                                 height=40,
                                                 command=lambda: menu_func(pagina_tampa_sim, menu))
        botao_tampa_receita_menu._set_appearance_mode("dark")
        botao_tampa_receita_menu.pack(side="bottom", pady=5)

        botao_tampa_receita_voltar = ctk.CTkButton(pagina_tampa_sim, text="Voltar", font=("Arial", 24), width=100,
                                                   height=40,
                                                   command=lambda: voltar_func(pagina_tampa_sim, pagina_tampa))
        botao_tampa_receita_voltar._set_appearance_mode("dark")
        botao_tampa_receita_voltar.pack(side="bottom", pady=5)

    label_tampa = ctk.CTkLabel(pagina_tampa, text="", font=("Arial", 24))
    label_tampa._set_appearance_mode("dark")
    label_tampa.pack(pady=170)

    label_pergunta = ctk.CTkLabel(pagina_tampa, width=300,
                                  text="Você tem pelo menos duas tampas de garrafa de plástico?",
                                  font=("Arial", 24))  # texto para fazer a primeira pergunta.
    label_pergunta._set_appearance_mode("dark")
    label_pergunta.pack(pady=20)

    botao_tampa_sim = ctk.CTkButton(pagina_tampa, text="SIM", width=200, command=sim,
                                    fg_color="green")  # Botão com a opção "SIM" que tem como comando a função sim().
    botao_tampa_sim._set_appearance_mode("dark")
    botao_tampa_sim.pack(pady=10)
    botao_tampa_nao = ctk.CTkButton(pagina_tampa, text="NÃO", width=200, command=nao,
                                    fg_color="red")  # Botão com a opção "SIM" que tem como comando a função nao().
    botao_tampa_nao._set_appearance_mode("dark")
    botao_tampa_nao.pack(pady=10)

    label_espaco = ctk.CTkLabel(pagina_tampa, text="")
    label_espaco._set_appearance_mode("dark")
    label_espaco.pack(side="bottom", pady=0)

    botao_tampa_menu = ctk.CTkButton(pagina_tampa, text="Menu", font=("Arial", 24), width=100, height=40,
                                     command=menu)
    botao_tampa_menu._set_appearance_mode("dark")
    botao_tampa_menu.pack(side="bottom", pady=5)

    botao_tampa_voltar = ctk.CTkButton(pagina_tampa, text="Voltar", font=("Arial", 24), width=100,
                                       height=40,
                                       command=voltar)
    botao_tampa_voltar._set_appearance_mode("dark")
    botao_tampa_voltar.pack(side="bottom", pady=5)

    return pagina_tampa