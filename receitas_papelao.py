import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk

def botao_receita(pagina, janela, menu, menu_func, voltar_func): # função do botão da receita.

    def receita(): # função da pagina da receita.

        pagina.pack_forget() # "Esquece" a página anterior ou fecha a página anterior.

        frame_receita_caixa_papelao = ctk.CTkFrame(janela) # Cria uma nova página.
        frame_receita_caixa_papelao._set_appearance_mode("dark")
        frame_receita_caixa_papelao.pack(fill="both", expand=True)

        label_receita_caixa_papelao = ctk.CTkLabel(frame_receita_caixa_papelao,  # Label que fala a receita.
                                                   text="Materiais: Uma caixa de papelão, papel decorativo ou jornal, tesoura, corda, borracha e silicone.", font= ("Arial", 25))
        label_receita_caixa_papelao._set_appearance_mode("dark")
        label_receita_caixa_papelao.pack(pady=20)

        imagem1 = ctk.CTkImage(light_image=Image.open("passo_1_cesto.jpeg"), size=(300, 200))
        imagem2 = ctk.CTkImage(light_image=Image.open("passo_2_cesto.jpeg"), size=(300, 200))
        imagem3 = ctk.CTkImage(light_image=Image.open("passo_3_cesto.jpeg"), size=(300, 200))
        imagem4 = ctk.CTkImage(light_image=Image.open("passo_4_cesto.jpeg"), size=(300, 200))
        imagem5 = ctk.CTkImage(light_image=Image.open("passo_5_cesto.jpeg"), size=(300, 200))

        abas = ctk.CTkTabview(frame_receita_caixa_papelao, segmented_button_fg_color="White", segmented_button_unselected_color="#8B4513", segmented_button_unselected_hover_color="#8B4513", segmented_button_selected_color="#654321")
        abas._set_appearance_mode("dark")
        abas.pack(pady=20)

        abas.add("Passo 1")
        abas.add("Passo 2")
        abas.add("Passo 3")
        abas.add("Passo 4")
        abas.add("Passo 5")

        label_passo1 = ctk.CTkLabel(abas.tab("Passo 1"), # Label com o primeiro passo.
                                    text="1. Pegue a caixa de papelão (de preferência uma caixa de papelão rígida) e faça 2 cortes em duas laterais para fazer as alças do cesto.", font=("Arial", 22))
        label_passo1._set_appearance_mode("dark")
        label_passo1.pack(pady=20)
        label_imagem1 = ctk.CTkLabel(abas.tab("Passo 1"), image=imagem1, text="") #Imagem do primeiro passo.
        label_imagem1.pack(pady=0)

        label_passo2 = ctk.CTkLabel(abas.tab("Passo 2"), # Label com o segundo passo.
                                    text="2. Envelope a caixa de papelão como preferir ou apenas pinte se quiser.", font=("Arial", 22))
        label_passo2._set_appearance_mode("dark")
        label_passo2.pack(pady=20)
        label_imagem2 = ctk.CTkLabel(abas.tab("Passo 2"), image=imagem2, text="") # Imagem do segundo passo.
        label_imagem2.pack(pady=0)

        label_passo3 = ctk.CTkLabel(abas.tab("Passo 3"), # Label com o terceiro passo.
                                    text="3. Passe fita no fundo da caixa para trazer mais resistência e dureza para o cesto.", font=("Arial", 22))
        label_passo3._set_appearance_mode("dark")
        label_passo3.pack(pady=20)
        label_imagem3 = ctk.CTkLabel(abas.tab("Passo 3"), image=imagem3, text="") # Imagem do terceiro passo.
        label_imagem3.pack(pady=0)

        label_passo4 = ctk.CTkLabel(abas.tab("Passo 4"), # Label com o quarto passo.
                                    text="4. Reforce o fundo as laterais da caixa, recortando outro papelão para mais firmeza e durabilidade.", font=("Arial", 22))
        label_passo4._set_appearance_mode("dark")
        label_passo4.pack(pady=20)
        label_imagem4 = ctk.CTkLabel(abas.tab("Passo 4"), image=imagem4, text="") # Imagem do quarto passo.
        label_imagem4.pack(pady=0)

        label_passo5 = ctk.CTkLabel(abas.tab("Passo 5"), # Label com o quinto passo.
                                    text="5. E por último, passe corda ou algum tipo de fita nas alças do cesto, para uma melhor estética.", font=("Arial", 22))
        label_passo5._set_appearance_mode("dark")
        label_passo5.pack(pady=20)
        label_imagem5 = ctk.CTkLabel(abas.tab("Passo 5"), image=imagem5, text="") # Imagem do quinto passo.
        label_imagem5.pack(pady=0)

        label_fonte = ctk.CTkLabel(frame_receita_caixa_papelao,
                                   text="Fonte: Canal GO GREEN - Youtube.",
                                   font=("Arial", 25), text_color="Grey")
        label_fonte._set_appearance_mode("dark")
        label_fonte.pack(pady=20)

        label_espaco = ctk.CTkLabel(frame_receita_caixa_papelao, text="") # Label que cria um espaço na página.
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(side="bottom", pady=0)

        botao_receita_menu = ctk.CTkButton(frame_receita_caixa_papelao, text="Menu", font=("Arial", 24), width=100,  # Botão que volta ao menu inicial dentro da página temporária.
                                           height=40,
                                           command=lambda: menu_func(frame_receita_caixa_papelao, menu))
        botao_receita_menu._set_appearance_mode("dark")
        botao_receita_menu.pack(side="bottom", pady=5)

        botao_receita_voltar = ctk.CTkButton(frame_receita_caixa_papelao, text="Voltar", font=("Arial", 24), width=100,  # Botão que volta á pagina anterior dentro da página temporária.
                                             height=40,
                                             command=lambda: voltar_func(frame_receita_caixa_papelao, pagina))
        botao_receita_voltar._set_appearance_mode("dark")
        botao_receita_voltar.pack(side="bottom", pady=5)

    botao_receita = ctk.CTkButton(pagina, text="Cesto para roupas sujas ou para guardar pequenas coisas", command=receita, # Botão com o nome da receita que tem como comando a função receita().
                                  fg_color="#8B4513", hover_color="#654321")
    botao_receita._set_appearance_mode("dark")

    return botao_receita # retorna o botão da receita.


def botao_receita2(pagina, janela, menu, menu_func, voltar_func): # função do botão da receita 2.

    def receita(): # função da pagina da receita 2.

        pagina.pack_forget() # "Esquece" a página anterior ou fecha a página anterior.

        frame_receita_caixa_papelao = ctk.CTkFrame(janela) # Cria uma nova página.
        frame_receita_caixa_papelao._set_appearance_mode("dark")
        frame_receita_caixa_papelao.pack(fill="both", expand=True)

        label_receita_caixa_papelao = ctk.CTkLabel(frame_receita_caixa_papelao, text="Materiais: Uma caixa de papelão, estilete ou tesoura, super cola.", font= ("Arial", 25))
        label_receita_caixa_papelao._set_appearance_mode("dark")
        label_receita_caixa_papelao.pack(pady=20)

        imagem1 = ctk.CTkImage(light_image=Image.open("passo_1_arranhador.jpeg"), size=(300, 200))
        imagem2 = ctk.CTkImage(light_image=Image.open("passo_2_arranhador.jpeg"), size=(300, 200))
        imagem3 = ctk.CTkImage(light_image=Image.open("passo_3_arranhador.jpeg"), size=(300, 200))
        imagem4 = ctk.CTkImage(light_image=Image.open("passo_4_arranhador.jpeg"), size=(300, 200))
        imagem5 = ctk.CTkImage(light_image=Image.open("passo_5_arranhador.jpeg"), size=(300, 200))

        abas = ctk.CTkTabview(frame_receita_caixa_papelao, segmented_button_fg_color="White", segmented_button_unselected_color="#8B4513", segmented_button_unselected_hover_color="#8B4513", segmented_button_selected_color="#654321")
        abas._set_appearance_mode("dark")
        abas.pack(pady=20)

        abas.add("Passo 1")
        abas.add("Passo 2")
        abas.add("Passo 3")
        abas.add("Passo 4")
        abas.add("Passo 5")

        label_passo1 = ctk.CTkLabel(abas.tab("Passo 1"),  # Label com o primeiro passo.
                                    text="1. Você precisará de uma caixa de papelão e precisará abri-la.",
                                    font=("Arial", 22))
        label_passo1._set_appearance_mode("dark")
        label_passo1.pack(pady=20)
        label_imagem1 = ctk.CTkLabel(abas.tab("Passo 1"), image=imagem1, text="")  # Imagem do primeiro passo.
        label_imagem1.pack(pady=0)

        label_passo2 = ctk.CTkLabel(abas.tab("Passo 2"),  # Label com o segundo passo.
                                    text="2. Corte a caixa em filetes de 8cm por 30cm.",
                                    font=("Arial", 22))
        label_passo2._set_appearance_mode("dark")
        label_passo2.pack(pady=20)
        label_imagem2 = ctk.CTkLabel(abas.tab("Passo 2"), image=imagem2, text="")  # Imagem do segundo passo.
        label_imagem2.pack(pady=0)

        label_passo3 = ctk.CTkLabel(abas.tab("Passo 3"),  # Label com o terceiro passo.
                                    text="3. Cole um filete do lado do outro.",
                                    font=("Arial", 22))
        label_passo3._set_appearance_mode("dark")
        label_passo3.pack(pady=20)
        label_imagem3 = ctk.CTkLabel(abas.tab("Passo 3"), image=imagem3, text="")  # Imagem do terceiro passo.
        label_imagem3.pack(pady=0)

        label_passo4 = ctk.CTkLabel(abas.tab("Passo 4"),  # Label com o quarto passo.
                                    text="4. De modo que no fim fique desse jeito.",
                                    font=("Arial", 22))
        label_passo4._set_appearance_mode("dark")
        label_passo4.pack(pady=20)
        label_imagem4 = ctk.CTkLabel(abas.tab("Passo 4"), image=imagem4, text="")  # Imagem do quarto passo.
        label_imagem4.pack(pady=0)

        label_passo5 = ctk.CTkLabel(abas.tab("Passo 5"),  # Label com o quinto passo.
                                    text="5. Pronto!! Agora seu gato não irá mais destruir o sofá.",
                                    font=("Arial", 22))
        label_passo5._set_appearance_mode("dark")
        label_passo5.pack(pady=20)
        label_imagem5 = ctk.CTkLabel(abas.tab("Passo 5"), image=imagem5, text="")  # Imagem do quinto passo.
        label_imagem5.pack(pady=0)

        label_fonte = ctk.CTkLabel(frame_receita_caixa_papelao,
                                                   text="Fonte: calisbruno - tiktok.",
                                                   font=("Arial", 25), text_color="Grey")
        label_fonte._set_appearance_mode("dark")
        label_fonte.pack(pady=20)


        label_espaco = ctk.CTkLabel(frame_receita_caixa_papelao, text="")
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(side="bottom", pady=10)

        botao_receita_menu = ctk.CTkButton(frame_receita_caixa_papelao, text="Menu", font=("Arial", 24), width=100,
                                           height=40,
                                           command=lambda: menu_func(frame_receita_caixa_papelao, menu))
        botao_receita_menu._set_appearance_mode("dark")
        botao_receita_menu.pack(side="bottom", pady=10)

        botao_receita_voltar = ctk.CTkButton(frame_receita_caixa_papelao, text="Voltar", font=("Arial", 24), width=100,
                                             height=40,
                                             command=lambda: voltar_func(frame_receita_caixa_papelao, pagina))
        botao_receita_voltar._set_appearance_mode("dark")
        botao_receita_voltar.pack(side="bottom", pady=0)

    botao_receita2 = ctk.CTkButton(pagina, text="Arranhador Para Gatos", command=receita, fg_color="#8B4513", hover_color="#654321")
    botao_receita2._set_appearance_mode("dark")
    return botao_receita2