import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk

def botao_receita(pagina, janela, menu, menu_func, voltar_func): # função do botão da receita.

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

        label_fonte = ctk.CTkLabel(frame_receita_garrafa_pet,
                                   text="Fonte: Tata Pereira - Youtube.",
                                   font=("Arial", 25), text_color="Grey")
        label_fonte._set_appearance_mode("dark")
        label_fonte.pack(pady=20)

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


def botao_receita2(pagina, janela, menu, menu_func, voltar_func): # função do botão da receita 2.

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
    return botao_receita2