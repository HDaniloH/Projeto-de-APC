import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
from receitas_plastico import fechar, fim_receita

def botao_receita_rolo(pagina, janela, menu, menu_func, voltar_func): # função do botão da receita.

    def receita(): # função da pagina da receita.

        pagina.pack_forget() # "Esquece" a página anterior ou fecha a página anterior.

        frame_receita_rolos = ctk.CTkFrame(janela) # Cria uma nova página.
        frame_receita_rolos._set_appearance_mode("dark")
        frame_receita_rolos.pack(fill="both", expand=True)

        label_receita_rolos = ctk.CTkLabel(frame_receita_rolos,  # Label que fala a receita.
                                           text="Materiais: Rolos de papel higiênico, tesoura, papel de embrulho, cola, fita adesiva para forrar e um pedaço de papelão para a base.", font= ("Arial", 25))
        label_receita_rolos._set_appearance_mode("dark")
        label_receita_rolos.pack(pady=50)

        imagem1 = ctk.CTkImage(light_image=Image.open("Imagens receita/receita_rolos.jpeg"), size=(300, 200)) # Imagem de apoio.
        label_imagem1 = ctk.CTkLabel(frame_receita_rolos, image=imagem1, text="")
        label_imagem1.pack(pady=20)

        abas = ctk.CTkTabview(frame_receita_rolos, segmented_button_fg_color="White", segmented_button_unselected_color="White", segmented_button_unselected_hover_color="White", segmented_button_selected_color="Grey", segmented_button_selected_hover_color="Grey", text_color="Black", height=150)
        abas._set_appearance_mode("dark")
        abas.pack(pady=0)

        abas.add("Passo 1")
        abas.add("Passo 2")
        abas.add("Passo 3")
        abas.add("Passo 4")
        abas.add("Passo 5")

        label_passo1 = ctk.CTkLabel(abas.tab("Passo 1"),  # Label com o primeiro passo.
                                    text="1. Corte o Rolo de papel para que fique do tamanho que deseja..",
                                    font=("Arial", 22))
        label_passo1._set_appearance_mode("dark")
        label_passo1.pack(pady=20)

        label_passo2 = ctk.CTkLabel(abas.tab("Passo 2"),  # Label com o segundo passo.
                                    text="2. Pinte ou decore o rolo da forma que preferir e espere secar.",
                                    font=("Arial", 22))
        label_passo2._set_appearance_mode("dark")
        label_passo2.pack(pady=20)

        label_passo3 = ctk.CTkLabel(abas.tab("Passo 3"),  # Label com o terceiro passo.
                                    text="3. Enquanto isso recorte um papelão no formato e tamanho do fundo.",
                                    font=("Arial", 22))
        label_passo3._set_appearance_mode("dark")
        label_passo3.pack(pady=20)

        label_passo4 = ctk.CTkLabel(abas.tab("Passo 4"),  # Label com o terceiro passo.
                                    text="4. Cole o fundo de papelão no rolo.",
                                    font=("Arial", 22))
        label_passo4._set_appearance_mode("dark")
        label_passo4.pack(pady=20)

        label_passo5 = ctk.CTkLabel(abas.tab("Passo 5"),  # Label com o terceiro passo.
                                    text="5. Após o rolo secar esta pronto!! Agora você tem um Porta-lápis.",
                                    font=("Arial", 22))
        label_passo5._set_appearance_mode("dark")
        label_passo5.pack(pady=20)

        label_fonte = ctk.CTkLabel(frame_receita_rolos,
                                   text="Fonte: Colhogar.",
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

def botao_receita_rolo2(pagina, janela, menu, menu_func, voltar_func): # função do botão da receita.

    def receita(): # função da pagina da receita.

        pagina.pack_forget() # "Esquece" a página anterior ou fecha a página anterior.

        frame_receita_rolos = ctk.CTkFrame(janela) # Cria uma nova página.
        frame_receita_rolos._set_appearance_mode("dark")
        frame_receita_rolos.pack(fill="both", expand=True)

        label_receita_rolos = ctk.CTkLabel(frame_receita_rolos,  # Label que fala a receita.
                                           text="Materiais: Pelo menos 1 rolo de papel e, para decorar, pode usar têmperas, marcadores ou papel colorido.", font= ("Arial", 25))
        label_receita_rolos._set_appearance_mode("dark")
        label_receita_rolos.pack(pady=50)

        imagem1 = ctk.CTkImage(light_image=Image.open("Imagens receita/braceletes_rolo.jpeg"), size=(300, 200)) # Imagem de apoio.
        label_imagem1 = ctk.CTkLabel(frame_receita_rolos, image=imagem1, text="")
        label_imagem1.pack(pady=20)

        abas = ctk.CTkTabview(frame_receita_rolos, segmented_button_fg_color="White", segmented_button_unselected_color="White", segmented_button_unselected_hover_color="White", segmented_button_selected_color="Grey", segmented_button_selected_hover_color="Grey", text_color="Black", height=150)
        abas._set_appearance_mode("dark")
        abas.pack(pady=0)

        abas.add("Passo 1")
        abas.add("Passo 2")
        abas.add("Passo 3")

        label_passo1 = ctk.CTkLabel(abas.tab("Passo 1"),  # Label com o primeiro passo.
                                    text="1. Pegue um rolo de papel higiênico ou corte um rolo de papel toalha no tamanho desejado.",
                                    font=("Arial", 22))
        label_passo1._set_appearance_mode("dark")
        label_passo1.pack(pady=20)

        label_passo2 = ctk.CTkLabel(abas.tab("Passo 2"),  # Label com o segundo passo.
                                    text="2. Pinte ou decore o rolo da forma que preferir e espere secar.",
                                    font=("Arial", 22))
        label_passo2._set_appearance_mode("dark")
        label_passo2.pack(pady=20)

        label_passo3 = ctk.CTkLabel(abas.tab("Passo 3"),  # Label com o terceiro passo.
                                    text="3. Após secar completamente está pronto o super bracelete para seus filhos!",
                                    font=("Arial", 22))
        label_passo3._set_appearance_mode("dark")
        label_passo3.pack(pady=20)

        label_fonte = ctk.CTkLabel(frame_receita_rolos,
                                   text="Fonte: Pequeocio. Disponível em: <https://www.pequeocio.com/7-manualidades-infantiles-rollos-papel/>",
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

    botao_receita2 = ctk.CTkButton(pagina, text="Braceletes de Rolo de Papel", command=receita, # Botão com o nome da receita que tem como comando a função receita().
                                  fg_color="White", hover_color="Grey", text_color="Black")
    botao_receita2._set_appearance_mode("dark")

    return botao_receita2 # retorna o botão da receita.

def botao_receita_papel(pagina, janela, menu, menu_func, voltar_func): # função do botão da receita.

    def receita(): # função da pagina da receita.

        pagina.pack_forget() # "Esquece" a página anterior ou fecha a página anterior.

        frame_receita_papel = ctk.CTkFrame(janela) # Cria uma nova página.
        frame_receita_papel._set_appearance_mode("dark")
        frame_receita_papel.pack(fill="both", expand=True)

        label_receita_papel = ctk.CTkLabel(frame_receita_papel,  # Label que fala a receita.
                                           text="Materiais: Uma folha de papel A4, régua, tesoura, cola e marcadores.", font= ("Arial", 25))
        label_receita_papel._set_appearance_mode("dark")
        label_receita_papel.pack(pady=50)

        imagem1 = ctk.CTkImage(light_image=Image.open("Imagens receita/parte_1_marcadores.jpeg"), size=(450, 200)) # Alocação de imagens a variáveis.
        imagem2 = ctk.CTkImage(light_image=Image.open("Imagens receita/parte_2_marcadores.jpeg"), size=(450, 200))
        imagem3 = ctk.CTkImage(light_image=Image.open("Imagens receita/parte_3_marcadores.jpeg"), size=(450, 200))


        abas = ctk.CTkTabview(frame_receita_papel, segmented_button_fg_color="White", segmented_button_unselected_color="White", segmented_button_unselected_hover_color="White", segmented_button_selected_color="Grey", segmented_button_selected_hover_color="Grey", text_color="Black")
        abas._set_appearance_mode("dark")
        abas.pack(pady=0)

        abas.add("Passo 1")
        abas.add("Passo 2")
        abas.add("Passo 3")

        label_passo1 = ctk.CTkLabel(abas.tab("Passo 1"),  # Label com o primeiro passo.
                                    text="1. Marque  a folha e dobre nas marcaçoes.",
                                    font=("Arial", 22))
        label_passo1._set_appearance_mode("dark")
        label_passo1.pack(pady=20)
        label_imagem1 = ctk.CTkLabel(abas.tab("Passo 1"), image=imagem1, text="")  # Imagem do primeiro passo.
        label_imagem1.pack(pady=0)

        label_passo2 = ctk.CTkLabel(abas.tab("Passo 2"),  # Label com o segundo passo.
                                    text="2. Apos marcar, corte e dobre.",
                                    font=("Arial", 22))
        label_passo2._set_appearance_mode("dark")
        label_passo2.pack(pady=20)
        label_imagem2 = ctk.CTkLabel(abas.tab("Passo 2"), image=imagem2, text="")  # Imagem do segundo passo.
        label_imagem2.pack(pady=0)

        label_passo3 = ctk.CTkLabel(abas.tab("Passo 3"),  # Label com o terceiro passo.
                                    text="3. Cole as duas orelhinhas que restaram, e decore como quiser.",
                                    font=("Arial", 22))
        label_passo3._set_appearance_mode("dark")
        label_passo3.pack(pady=20)
        label_imagem3 = ctk.CTkLabel(abas.tab("Passo 3"), image=imagem3, text="")  # Imagem do terceiro passo.
        label_imagem3.pack(pady=0)

        label_fonte = ctk.CTkLabel(frame_receita_papel,
                                   text="Fonte: maynterest. Disponível em: <https://www.youtube.com/@maynterest>",
                                   font=("Arial", 25), text_color="Grey")
        label_fonte._set_appearance_mode("dark")
        label_fonte.pack(pady=20)

        label_espaco = ctk.CTkLabel(frame_receita_papel, text="") # Label que cria um espaço na página.
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(side="bottom", pady=0)

        botao_fim = ctk.CTkButton(frame_receita_papel, text="Fim", font=("Arial", 24), width=100,  # Botão que avança para a página final.
                                  height=40, text_color="White", fg_color="Red",
                                  command=lambda: fim_receita(frame_receita_papel, janela, menu, menu_func, voltar_func))
        botao_fim._set_appearance_mode("dark")
        botao_fim.pack(side="bottom", pady=5)

        botao_receita_menu = ctk.CTkButton(frame_receita_papel, text="Menu", font=("Arial", 24), width=100,  # Botão que volta ao menu inicial dentro da página temporária.
                                           height=40,
                                           command=lambda: menu_func(frame_receita_papel, menu))
        botao_receita_menu._set_appearance_mode("dark")
        botao_receita_menu.pack(side="bottom", pady=5)

        botao_receita_voltar = ctk.CTkButton(frame_receita_papel, text="Voltar", font=("Arial", 24), width=100,  # Botão que volta á pagina anterior dentro da página temporária.
                                             height=40,
                                             command=lambda: voltar_func(frame_receita_papel, pagina))
        botao_receita_voltar._set_appearance_mode("dark")
        botao_receita_voltar.pack(side="bottom", pady=5)

    botao_receita_p = ctk.CTkButton(pagina, text="Marcadores para livros", command=receita,  # Botão com o nome da receita que tem como comando a função receita().
                                        fg_color="White", hover_color="Grey", text_color="Black")
    botao_receita_p._set_appearance_mode("dark")

    return botao_receita_p # retorna o botão da receita.

def botao_receita_papel2(pagina, janela, menu, menu_func, voltar_func): # função do botão da receita.

    def receita(): # função da pagina da receita.

        pagina.pack_forget() # "Esquece" a página anterior ou fecha a página anterior.

        frame_receita_papel = ctk.CTkFrame(janela) # Cria uma nova página.
        frame_receita_papel._set_appearance_mode("dark")
        frame_receita_papel.pack(fill="both", expand=True)

        label_receita_papel = ctk.CTkLabel(frame_receita_papel,  # Label que fala a receita.
                                           text="Materiais: Duas folhas de papel, tesoura e cola.", font= ("Arial", 25))
        label_receita_papel._set_appearance_mode("dark")
        label_receita_papel.pack(pady=50)

        imagem1 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_1_livreto.png"), size=(500, 200)) # Alocação de imagens a variáveis.
        imagem2 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_2_livreto.png"), size=(500, 200))
        imagem3 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_3_livreto.png"), size=(500, 200))
        imagem4 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_4_livreto.png"), size=(500, 200))
        imagem5 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_5_livreto.png"), size=(500, 200))
        imagem6 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_6_livreto.png"), size=(500, 200))
        imagem7 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_7_livreto.png"), size=(500, 200))


        abas = ctk.CTkTabview(frame_receita_papel, segmented_button_fg_color="White", segmented_button_unselected_color="White", segmented_button_unselected_hover_color="White", segmented_button_selected_color="Grey", segmented_button_selected_hover_color="Grey", text_color="Black")
        abas._set_appearance_mode("dark")
        abas.pack(pady=0)

        abas.add("Passo 1")
        abas.add("Passo 2")
        abas.add("Passo 3")
        abas.add("Passo 4")
        abas.add("Passo 5")
        abas.add("Passo 6")
        abas.add("Passo 7")

        label_passo1 = ctk.CTkLabel(abas.tab("Passo 1"),  # Label com o primeiro passo.
                                    text="1. Dobre uma folha A4 na vertical e dobre outras vezes de modo que fique desse jeito:", font=("Arial", 22))
        label_passo1._set_appearance_mode("dark")
        label_passo1.pack(pady=20)
        label_imagem1 = ctk.CTkLabel(abas.tab("Passo 1"), image=imagem1, text="")  # Imagem do primeiro passo.
        label_imagem1.pack(pady=0)

        label_passo2 = ctk.CTkLabel(abas.tab("Passo 2"),  # Label com o segundo passo.
                                    text="2. Corte a folha dividindo ela em filetes e começe a dobrar eles dessa forma:", font=("Arial", 22))
        label_passo2._set_appearance_mode("dark")
        label_passo2.pack(pady=20)
        label_imagem2 = ctk.CTkLabel(abas.tab("Passo 2"), image=imagem2, text="")  # Imagem do segundo passo.
        label_imagem2.pack(pady=0)

        label_passo3 = ctk.CTkLabel(abas.tab("Passo 3"),  # Label com o terceiro passo.
                                    text="3. Dobre o filete em safona e passe cola nas extremidades.",
                                    font=("Arial", 22))
        label_passo3._set_appearance_mode("dark")
        label_passo3.pack(pady=20)
        label_imagem3 = ctk.CTkLabel(abas.tab("Passo 3"), image=imagem3, text="")  # Imagem do terceiro passo.
        label_imagem3.pack(pady=0)

        label_passo4 = ctk.CTkLabel(abas.tab("Passo 4"),  # Label com o quarto passo.
                                    text="4. Comece a pressionar as dobras para garantir que o livreto fique bem alinhado e fixo.", font=("Arial", 22))
        label_passo4._set_appearance_mode("dark")
        label_passo4.pack(pady=20)
        label_imagem4 = ctk.CTkLabel(abas.tab("Passo 4"), image=imagem4, text="")  # Imagem do quarto passo.
        label_imagem4.pack(pady=0)

        label_passo5 = ctk.CTkLabel(abas.tab("Passo 5"),  # Label com o quinto passo.
                                    text="5. Pegue um outro papel da cor que preferir e dobre para que fique desse jeito:",
                                    font=("Arial", 22))
        label_passo5._set_appearance_mode("dark")
        label_passo5.pack(pady=20)
        label_imagem5 = ctk.CTkLabel(abas.tab("Passo 5"), image=imagem5, text="")  # Imagem do quinto passo.
        label_imagem5.pack(pady=0)

        label_passo6 = ctk.CTkLabel(abas.tab("Passo 6"),  # Label com o sexto passo.
                                    text="6. Junte os filetes dobrados com a capa e dobre a parte que esta sobrando para dentro.",
                                    font=("Arial", 22))
        label_passo6._set_appearance_mode("dark")
        label_passo6.pack(pady=20)
        label_imagem6 = ctk.CTkLabel(abas.tab("Passo 6"), image=imagem6, text="")  # Imagem do sexto passo.
        label_imagem6.pack(pady=0)

        label_passo7 = ctk.CTkLabel(abas.tab("Passo 7"),  # Label com o setimo passo.
                                    text="7. Agora seu mini livreto está pronto! Você pode usá-lo para anotações, desenhos ou até como um pequeno álbum de figurinhas.",
                                    font=("Arial", 22))
        label_passo7._set_appearance_mode("dark")
        label_passo7.pack(pady=20)
        label_imagem7 = ctk.CTkLabel(abas.tab("Passo 7"), image=imagem7, text="")  # Imagem do setimo passo.
        label_imagem7.pack(pady=0)

        label_fonte = ctk.CTkLabel(frame_receita_papel,
                                   text="Fonte: Innova manualidades. Disponível em: <www.youtube.com/@InnovaManualidades>",
                                   font=("Arial", 25), text_color="Grey")
        label_fonte._set_appearance_mode("dark")
        label_fonte.pack(pady=20)

        label_espaco = ctk.CTkLabel(frame_receita_papel, text="") # Label que cria um espaço na página.
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(side="bottom", pady=0)

        botao_fim = ctk.CTkButton(frame_receita_papel, text="Fim", font=("Arial", 24), width=100,  # Botão que avança para a página final.
                                  height=40, text_color="White", fg_color="Red",
                                  command=lambda: fim_receita(frame_receita_papel, janela, menu, menu_func, voltar_func))
        botao_fim._set_appearance_mode("dark")
        botao_fim.pack(side="bottom", pady=5)

        botao_receita_menu = ctk.CTkButton(frame_receita_papel, text="Menu", font=("Arial", 24), width=100,  # Botão que volta ao menu inicial dentro da página temporária.
                                           height=40,
                                           command=lambda: menu_func(frame_receita_papel, menu))
        botao_receita_menu._set_appearance_mode("dark")
        botao_receita_menu.pack(side="bottom", pady=5)

        botao_receita_voltar = ctk.CTkButton(frame_receita_papel, text="Voltar", font=("Arial", 24), width=100,  # Botão que volta á pagina anterior dentro da página temporária.
                                             height=40,
                                             command=lambda: voltar_func(frame_receita_papel, pagina))
        botao_receita_voltar._set_appearance_mode("dark")
        botao_receita_voltar.pack(side="bottom", pady=5)

    botao_receita_p2 = ctk.CTkButton(pagina, text="Mini Livretos", command=receita,  # Botão com o nome da receita que tem como comando a função receita().
                                        fg_color="White", hover_color="Grey", text_color="Black")
    botao_receita_p2._set_appearance_mode("dark")

    return botao_receita_p2 # retorna o botão da receita.

def botao_receita_jornal(pagina, janela, menu, menu_func, voltar_func): # função do botão da receita.

    def receita(): # função da pagina da receita.

        pagina.pack_forget() # "Esquece" a página anterior ou fecha a página anterior.

        frame_receita_papel = ctk.CTkFrame(janela) # Cria uma nova página.
        frame_receita_papel._set_appearance_mode("dark")
        frame_receita_papel.pack(fill="both", expand=True)

        label_receita_papel = ctk.CTkLabel(frame_receita_papel,  # Label que fala a receita.
                                           text="Materiais: Pelo menos uma folha de jornal, cola, fita adesiva ou decorativa, tesoura, pinças ou prendedores.",
                                           font=("Arial", 25))
        label_receita_papel._set_appearance_mode("dark")
        label_receita_papel.pack(pady=50)

        imagem = ctk.CTkImage(light_image=Image.open("Imagens receita/bolsas_jornal.jpeg"), # Imagem de apoio.
                              size=(300, 200))
        label_imagem = ctk.CTkLabel(frame_receita_papel, image=imagem, text="")
        label_imagem.pack(pady=0)

        abas = ctk.CTkTabview(frame_receita_papel, segmented_button_fg_color="White",
                              segmented_button_unselected_color="White",
                              segmented_button_unselected_hover_color="White", segmented_button_selected_color="Grey",
                              segmented_button_selected_hover_color="Grey", text_color="Black", height=150)
        abas._set_appearance_mode("dark")
        abas.pack(pady=20)

        abas.add("Passo 1")
        abas.add("Passo 2")
        abas.add("Passo 3")
        abas.add("Passo 4")
        abas.add("Passo 5")
        abas.add("Passo 6")
        abas.add("Passo 7")

        label_passo1 = ctk.CTkLabel(abas.tab("Passo 1"),  # Label com o primeiro passo.
                                    text="1. Pegue uma folha de jornal e corte no tamanho desejado.",
                                    font=("Arial", 22))
        label_passo1._set_appearance_mode("dark")
        label_passo1.pack(pady=20)

        label_passo2 = ctk.CTkLabel(abas.tab("Passo 2"),  # Label com o segundo passo.
                                    text="2. Dobre as laterais para formar um tubo, sobreponha um pouco e cole.",
                                    font=("Arial", 22))
        label_passo2._set_appearance_mode("dark")
        label_passo2.pack(pady=20)

        label_passo3 = ctk.CTkLabel(abas.tab("Passo 3"),  # Label com o terceiro passo.
                                    text="3. Para criar o fundo da bolsa, dobre a parte inferior para cima, formando uma aba larga.",
                                    font=("Arial", 22))
        label_passo3._set_appearance_mode("dark")
        label_passo3.pack(pady=20)

        label_passo4 = ctk.CTkLabel(abas.tab("Passo 4"),  # Label com o quarto passo.
                                    text="4. Abra essa aba e dobre as laterais para dentro, formando um formato de losango.",
                                    font=("Arial", 22))
        label_passo4._set_appearance_mode("dark")
        label_passo4.pack(pady=20)

        label_passo5 = ctk.CTkLabel(abas.tab("Passo 5"),  # Label com o quinto passo.
                                    text="5. Dobre as pontas superior e inferior para o centro e cole bem para fixar.",
                                    font=("Arial", 22))
        label_passo5._set_appearance_mode("dark")
        label_passo5.pack(pady=20)

        label_passo6 = ctk.CTkLabel(abas.tab("Passo 6"),  # Label com o sexto passo.
                                    text="6. Dobre a parte de cima para trás e prenda com algum tipo de prendedor ou fita.",
                                    font=("Arial", 22))
        label_passo6._set_appearance_mode("dark")
        label_passo6.pack(pady=20)

        label_passo7 = ctk.CTkLabel(abas.tab("Passo 7"),  # Label com o setimo passo.
                                    text="7. Decore da maneira que quiser e pronto!! Agora você tem uma mini bolsa de jornal.",
                                    font=("Arial", 22))
        label_passo7._set_appearance_mode("dark")
        label_passo7.pack(pady=20)

        label_fonte = ctk.CTkLabel(frame_receita_papel,
                                   text="Fonte: Craft and creativity",
                                   font=("Arial", 25), text_color="Grey")
        label_fonte._set_appearance_mode("dark")
        label_fonte.pack(pady=20)

        label_espaco = ctk.CTkLabel(frame_receita_papel, text="") # Label que cria um espaço na página.
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(side="bottom", pady=0)

        botao_fim = ctk.CTkButton(frame_receita_papel, text="Fim", font=("Arial", 24), width=100,  # Botão que avança para a página final.
                                  height=40, text_color="White", fg_color="Red",
                                  command=lambda: fim_receita(frame_receita_papel, janela, menu, menu_func, voltar_func))
        botao_fim._set_appearance_mode("dark")
        botao_fim.pack(side="bottom", pady=5)

        botao_receita_menu = ctk.CTkButton(frame_receita_papel, text="Menu", font=("Arial", 24), width=100,  # Botão que volta ao menu inicial dentro da página temporária.
                                           height=40,
                                           command=lambda: menu_func(frame_receita_papel, menu))
        botao_receita_menu._set_appearance_mode("dark")
        botao_receita_menu.pack(side="bottom", pady=5)

        botao_receita_voltar = ctk.CTkButton(frame_receita_papel, text="Voltar", font=("Arial", 24), width=100,  # Botão que volta á pagina anterior dentro da página temporária.
                                             height=40,
                                             command=lambda: voltar_func(frame_receita_papel, pagina))
        botao_receita_voltar._set_appearance_mode("dark")
        botao_receita_voltar.pack(side="bottom", pady=5)

    botao_receita_p3 = ctk.CTkButton(pagina, text="Mini Bolsa de Jornal", command=receita,  # Botão com o nome da receita que tem como comando a função receita().
                                        fg_color="White", hover_color="Grey", text_color="Black")
    botao_receita_p3._set_appearance_mode("dark")

    return botao_receita_p3 # retorna o botão da receita.

def botao_receita_jornal2(pagina, janela, menu, menu_func, voltar_func): # função do botão da receita.

    def receita(): # função da pagina da receita.

        pagina.pack_forget() # "Esquece" a página anterior ou fecha a página anterior.

        frame_receita_papel = ctk.CTkFrame(janela) # Cria uma nova página.
        frame_receita_papel._set_appearance_mode("dark")
        frame_receita_papel.pack(fill="both", expand=True)

        label_receita_papel = ctk.CTkLabel(frame_receita_papel,  # Label que fala a receita.
                                           text="Materiais: Folhas de jornal, papelão, tesouras e elementos decorativos de acordo com seu gosto.", font= ("Arial", 25))
        label_receita_papel._set_appearance_mode("dark")
        label_receita_papel.pack(pady=50)

        imagem = ctk.CTkImage(light_image=Image.open("Imagens receita/quadro_folha_papelao.png"), size=(170, 350)) # Imagem de apoio.
        label_imagem = ctk.CTkLabel(frame_receita_papel, image=imagem, text="")
        label_imagem.pack(pady=0)

        abas = ctk.CTkTabview(frame_receita_papel, segmented_button_fg_color="White", segmented_button_unselected_color="White", segmented_button_unselected_hover_color="White", segmented_button_selected_color="Grey", segmented_button_selected_hover_color="Grey", text_color="Black", height=150)
        abas._set_appearance_mode("dark")
        abas.pack(pady=20)

        abas.add("Passo 1")
        abas.add("Passo 2")
        abas.add("Passo 3")
        abas.add("Passo 4")

        label_passo1 = ctk.CTkLabel(abas.tab("Passo 1"),  # Label com o primeiro passo.
                                    text="1. Recorte a folha de jornal no formato do papelão.",
                                    font=("Arial", 22))
        label_passo1._set_appearance_mode("dark")
        label_passo1.pack(pady=20)

        label_passo2 = ctk.CTkLabel(abas.tab("Passo 2"),  # Label com o segundo passo.
                                    text="2. Cole a folha no papelão.",
                                    font=("Arial", 22))
        label_passo2._set_appearance_mode("dark")
        label_passo2.pack(pady=20)

        label_passo3 = ctk.CTkLabel(abas.tab("Passo 3"),  # Label com o terceiro passo.
                                    text="3. Decore da forma que quiser.",
                                    font=("Arial", 22))
        label_passo3._set_appearance_mode("dark")
        label_passo3.pack(pady=20)

        label_passo4 = ctk.CTkLabel(abas.tab("Passo 4"),  # Label com o quarto passo.
                                    text="4. E pronto!! Agora você tem um quadro.",
                                    font=("Arial", 22))
        label_passo4._set_appearance_mode("dark")
        label_passo4.pack(pady=20)

        label_fonte = ctk.CTkLabel(frame_receita_papel,
                                   text="Fonte: Manualidadescon",
                                   font=("Arial", 25), text_color="Grey")
        label_fonte._set_appearance_mode("dark")
        label_fonte.pack(pady=20)

        label_espaco = ctk.CTkLabel(frame_receita_papel, text="") # Label que cria um espaço na página.
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(side="bottom", pady=0)

        botao_fim = ctk.CTkButton(frame_receita_papel, text="Fim", font=("Arial", 24), width=100,  # Botão que avança para a página final.
                                  height=40, text_color="White", fg_color="Red",
                                  command=lambda: fim_receita(frame_receita_papel, janela, menu, menu_func, voltar_func))
        botao_fim._set_appearance_mode("dark")
        botao_fim.pack(side="bottom", pady=5)

        botao_receita_menu = ctk.CTkButton(frame_receita_papel, text="Menu", font=("Arial", 24), width=100,  # Botão que volta ao menu inicial dentro da página temporária.
                                           height=40,
                                           command=lambda: menu_func(frame_receita_papel, menu))
        botao_receita_menu._set_appearance_mode("dark")
        botao_receita_menu.pack(side="bottom", pady=5)

        botao_receita_voltar = ctk.CTkButton(frame_receita_papel, text="Voltar", font=("Arial", 24), width=100,  # Botão que volta á pagina anterior dentro da página temporária.
                                             height=40,
                                             command=lambda: voltar_func(frame_receita_papel, pagina))
        botao_receita_voltar._set_appearance_mode("dark")
        botao_receita_voltar.pack(side="bottom", pady=5)

    botao_receita_p3 = ctk.CTkButton(pagina, text="Quadro com Jornal", command=receita,  # Botão com o nome da receita que tem como comando a função receita().
                                        fg_color="White", hover_color="Grey", text_color="Black")
    botao_receita_p3._set_appearance_mode("dark")

    return botao_receita_p3 # retorna o botão da receita.