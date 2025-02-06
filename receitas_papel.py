import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk

def fechar():
    exit()

def fim_receita(pagina_receita, janela, menu, menu_func, voltar_func):

    pagina_receita.pack_forget()

    pagina_final = ctk.CTkFrame(janela)  # Cria uma nova página.
    pagina_final._set_appearance_mode("dark")
    pagina_final.pack(fill="both", expand=True)

    label_espaco = ctk.CTkLabel(pagina_final,  # Label de espaço na pagina final
                               text="")
    label_espaco._set_appearance_mode("dark")
    label_espaco.pack(pady=50)

    label_final = ctk.CTkLabel(pagina_final,  # Label final
                               text="Chegamos ao fim..",
                               font=("Arial", 40))
    label_final._set_appearance_mode("dark")
    label_final.pack(pady=10)

    label_final2 = ctk.CTkLabel(pagina_final,  # Label final
                               text="Obrigado por ter usado o nosso programa!",
                               font=("Arial", 30))
    label_final2._set_appearance_mode("dark")
    label_final2.pack(pady=10)

    label_final3 = ctk.CTkLabel(pagina_final,  # Label final
                                text="Com isso, você está ajudando não só a si mesmo,",
                                font=("Arial", 30))
    label_final3._set_appearance_mode("dark")
    label_final3.pack(pady=10)

    label_final4 = ctk.CTkLabel(pagina_final,  # Label final
                                text="mas também ao nosso mundo.",
                                font=("Arial", 30))
    label_final4._set_appearance_mode("dark")
    label_final4.pack(pady=10)

    label_espaco = ctk.CTkLabel(pagina_final, text="")  # Label que cria um espaço na página.
    label_espaco._set_appearance_mode("dark")
    label_espaco.pack(side="bottom", pady=0)

    botao_fechar = ctk.CTkButton(pagina_final, text="FECHAR", font=("Arial", 24), width=100,  # Botão que finaliza o programa.
                                           height=40, text_color="White", fg_color="Red",
                                           command=fechar)
    botao_fechar._set_appearance_mode("dark")
    botao_fechar.pack(side="bottom", pady=5)

    botao_final_menu = ctk.CTkButton(pagina_final, text="Menu", font=("Arial", 24), width=100,  # Botão que volta ao menu inicial dentro da página temporária.
                                     height=40,
                                     command=lambda: menu_func(pagina_final, menu))
    botao_final_menu._set_appearance_mode("dark")
    botao_final_menu.pack(side="bottom", pady=5)

    botao_final_voltar = ctk.CTkButton(pagina_final, text="Voltar", font=("Arial", 24), width=100,  # Botão que volta á pagina anterior dentro da página temporária.
                                       height=40,
                                       command=lambda: voltar_func(pagina_final, pagina_receita))
    botao_final_voltar._set_appearance_mode("dark")
    botao_final_voltar.pack(side="bottom", pady=5)


def botao_receita(pagina, janela, menu, menu_func, voltar_func): # função do botão da receita.

    def receita(): # função da pagina da receita.

        pagina.pack_forget() # "Esquece" a página anterior ou fecha a página anterior.

        frame_receita_rolos = ctk.CTkFrame(janela) # Cria uma nova página.
        frame_receita_rolos._set_appearance_mode("dark")
        frame_receita_rolos.pack(fill="both", expand=True)

        label_receita_rolos = ctk.CTkLabel(frame_receita_rolos,  # Label que fala a receita.
                                           text="Materiais: Rolos de papel higiênico, tesoura, papel de embrulho, fita adesiva para forrar, um pedaço de papelão para a base e silicone.", font= ("Arial", 25))
        label_receita_rolos._set_appearance_mode("dark")
        label_receita_rolos.pack(pady=50)

        imagem1 = ctk.CTkImage(light_image=Image.open("Imagens receita/receita_rolos.jpeg"), size=(300, 200))

        abas = ctk.CTkTabview(frame_receita_rolos, segmented_button_fg_color="White", segmented_button_unselected_color="White", segmented_button_unselected_hover_color="#White", segmented_button_selected_color="Grey", segmented_button_selected_hover_color="Grey", text_color="Black")
        abas._set_appearance_mode("dark")
        abas.pack(pady=0)

        abas.add("Imagem de apoio")

        label_imagem1 = ctk.CTkLabel(abas.tab("Imagem de apoio"), image=imagem1, text="") #Imagem do primeiro passo.
        label_imagem1.pack(pady=20)

        label_fonte = ctk.CTkLabel(frame_receita_rolos,
                                   text="Fonte: Canal GO GREEN - Youtube.",
                                   font=("Arial", 25), text_color="Grey")
        label_fonte._set_appearance_mode("dark")
        label_fonte.pack(pady=20)

        label_espaco = ctk.CTkLabel(frame_receita_rolos, text="") # Label que cria um espaço na página.
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(side="bottom", pady=0)

        botao_fim = ctk.CTkButton(frame_receita_rolos, text="Fim", font=("Arial", 24), width=100,  # Botão que avança para a página final.
                                  height=40, text_color="White", fg_color="Red",
                                  command=lambda: fim_receita(frame_receita_rolos, janela, menu, menu_func, voltar_func))
        botao_fim._set_appearance_mode("dark")
        botao_fim.pack(side="bottom", pady=5)

        botao_receita_menu = ctk.CTkButton(frame_receita_rolos, text="Menu", font=("Arial", 24), width=100,  # Botão que volta ao menu inicial dentro da página temporária.
                                           height=40,
                                           command=lambda: menu_func(frame_receita_rolos, menu))
        botao_receita_menu._set_appearance_mode("dark")
        botao_receita_menu.pack(side="bottom", pady=5)

        botao_receita_voltar = ctk.CTkButton(frame_receita_rolos, text="Voltar", font=("Arial", 24), width=100,  # Botão que volta á pagina anterior dentro da página temporária.
                                             height=40,
                                             command=lambda: voltar_func(frame_receita_rolos, pagina))
        botao_receita_voltar._set_appearance_mode("dark")
        botao_receita_voltar.pack(side="bottom", pady=5)

    botao_receita = ctk.CTkButton(pagina, text="Porta-lápis com rolos de papel higiênico", command=receita, # Botão com o nome da receita que tem como comando a função receita().
                                  fg_color="White", hover_color="Grey", text_color="Black")
    botao_receita._set_appearance_mode("dark")

    return botao_receita # retorna o botão da receita.