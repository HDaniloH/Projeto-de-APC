import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
from receitas_plastico import fechar, fim_receita

def botao_receita_maior(pagina, janela, menu, menu_func, voltar_func): # função do botão da receita.

    def receita(): # função da pagina da receita.

        pagina.pack_forget() # "Esquece" a página anterior ou fecha a página anterior.

        frame_receita_vidro = ctk.CTkFrame(janela) # Cria uma nova página.
        frame_receita_vidro._set_appearance_mode("dark")
        frame_receita_vidro.pack(fill="both", expand=True)

        label_receita_vidro = ctk.CTkLabel(frame_receita_vidro,  # Label que fala a receita.
                                           text="Materiais: Garrafa de vidro, barbante, água, balde ou recipiente grande, acetona, fogo, terra, planta e manta bidim, tnt, ou outro material sintético", font= ("Arial", 25))
        label_receita_vidro._set_appearance_mode("dark")
        label_receita_vidro.pack(pady=50)

        imagem2 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_1_autoirrigavel.jpeg"), size=(170, 170)) # Alocação de imagens a uma variável.
        imagem1 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_2_autoirrigavel.jpeg"), size=(170, 170))
        imagem3 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_3_autoirrigavel.jpeg"), size=(170, 170))
        imagem4 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_4_autoirrigavel.jpeg"), size=(170, 170))
        imagem5 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_5_autoirrigavel.jpeg"), size=(170, 170))
        imagem6 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_6_autoirrigavel.jpeg"), size=(170, 170))
        imagem7 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_7_autoirrigavel.jpeg"), size=(170, 170))
        imagem8 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_8_autoirrigavel.jpeg"), size=(170, 170))
        imagem9 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_9_autoirrigavel.jpeg"), size=(170, 170))
        imagem10 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_10_autoirrigavel.jpeg"), size=(170, 170))
        imagem11 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_11_autoirrigavel.jpeg"), size=(170, 170))
        imagem12 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_12_autoirrigavel.jpeg"), size=(170, 170))
        imagem13 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_13_autoirrigavel.jpeg"), size=(170, 170))
        imagem14 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_14_autoirrigavel.jpeg"), size=(170, 170))
        imagem15 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_15_autoirrigavel.jpeg"), size=(130, 130))

        abas = ctk.CTkTabview(frame_receita_vidro, segmented_button_fg_color="White", segmented_button_unselected_color="#CED4DA",  # criação de abas dentro da pagina.
                              segmented_button_unselected_hover_color="#CED4DA", segmented_button_selected_color="#6C757D", text_color="Black", segmented_button_selected_hover_color="#6C757D")
        abas._set_appearance_mode("dark")
        abas.pack(pady=0)

        abas.add("Passo 1") # Adicionando os nomes das abas.
        abas.add("Passo 2")
        abas.add("Passo 3")
        abas.add("Passo 4")
        abas.add("Passo 5")
        abas.add("Passo 6")
        abas.add("Passo 7")

        label_passo1 = ctk.CTkLabel(abas.tab("Passo 1"), # Label com o primeiro passo.
                                    text="1. Marque uma linha na metade da garrafa.", font=("Arial", 22))
        label_passo1._set_appearance_mode("dark")
        label_passo1.pack(pady=20)
        label_imagem1 = ctk.CTkLabel(abas.tab("Passo 1"), image=imagem1, text="") #Imagem do primeiro passo.
        label_imagem1.pack(pady=0)

        label_passo2 = ctk.CTkLabel(abas.tab("Passo 2"), # Label com o segundo passo.
                                    text="2. Amarre o barbante na linha marcada.", font=("Arial", 22))
        label_passo2._set_appearance_mode("dark")
        label_passo2.pack(pady=20)
        label_imagem2 = ctk.CTkLabel(abas.tab("Passo 2"), image=imagem2, text="") # Imagem do segundo passo.
        label_imagem2.pack(pady=0)

        label_passo3 = ctk.CTkLabel(abas.tab("Passo 3"), # Label com o terceiro passo.
                                    text="3. Encha de água até a marca.", font=("Arial", 22))
        label_passo3._set_appearance_mode("dark")
        label_passo3.pack(pady=20)
        label_imagem3 = ctk.CTkLabel(abas.tab("Passo 3"), image=imagem3, text="") # Imagem do terceiro passo.
        label_imagem3.pack(pady=0)

        label_passo4 = ctk.CTkLabel(abas.tab("Passo 4"), # Label com o quarto passo.
                                    text="4. Retire o círculo de barbante.", font=("Arial", 22))
        label_passo4._set_appearance_mode("dark")
        label_passo4.pack(pady=20)
        label_imagem4 = ctk.CTkLabel(abas.tab("Passo 4"), image=imagem4, text="") # Imagem do quarto passo.
        label_imagem4.pack(pady=0)

        label_passo5 = ctk.CTkLabel(abas.tab("Passo 5"), # Label com o quinto passo.
                                    text="5. Mergulhe-o em um pote com acetona.", font=("Arial", 22))
        label_passo5._set_appearance_mode("dark")
        label_passo5.pack(pady=20)
        label_imagem5 = ctk.CTkLabel(abas.tab("Passo 5"), image=imagem5, text="") # Imagem do quinto passo.
        label_imagem5.pack(pady=0)

        label_passo6 = ctk.CTkLabel(abas.tab("Passo 6"),  # Label com o quinto passo.
                                    text="6. Limpe as mãos e os resquícios de acetona.",
                                    font=("Arial", 22))
        label_passo6._set_appearance_mode("dark")
        label_passo6.pack(pady=20)
        label_imagem6 = ctk.CTkLabel(abas.tab("Passo 6"), image=imagem6, text="")  # Imagem do quinto passo.
        label_imagem6.pack(pady=0)

        label_passo7 = ctk.CTkLabel(abas.tab("Passo 7"),  # Label com o quinto passo.
                                    text="7. Ateie fogo no barbante",
                                    font=("Arial", 22))
        label_passo7._set_appearance_mode("dark")
        label_passo7.pack(pady=20)
        label_imagem7 = ctk.CTkLabel(abas.tab("Passo 7"), image=imagem7, text="")  # Imagem do quinto passo.
        label_imagem7.pack(pady=0)

        abas2 = ctk.CTkTabview(frame_receita_vidro, segmented_button_fg_color="White",
                              segmented_button_unselected_color="#CED4DA",  # criação de abas dentro da pagina.
                              segmented_button_unselected_hover_color="#CED4DA",
                              segmented_button_selected_color="#6C757D", text_color="Black",
                              segmented_button_selected_hover_color="#6C757D")
        abas2._set_appearance_mode("dark")
        abas2.pack(pady=20)

        abas2.add("Passo 8")
        abas2.add("Passo 9")
        abas2.add("Passo 10")
        abas2.add("Passo 11")
        abas2.add("Passo 12")
        abas2.add("Passo 13")
        abas2.add("Passo 14")
        abas2.add("Passo 15")

        label_passo8 = ctk.CTkLabel(abas2.tab("Passo 8"),  # Label com o primeiro passo.
                                    text="8. Assim que o barbante escurecer e o fogo abaixar, mergulhe a garrafa em um balde com água.", font=("Arial", 22))
        label_passo8._set_appearance_mode("dark")
        label_passo8.pack(pady=20)
        label_imagem8 = ctk.CTkLabel(abas2.tab("Passo 8"), image=imagem8, text="")  # Imagem do primeiro passo.
        label_imagem8.pack(pady=0)

        label_passo9 = ctk.CTkLabel(abas2.tab("Passo 9"),  # Label com o segundo passo.
                                    text="9. A garrafa irá quebrar devido ao choque térmico.", font=("Arial", 22))
        label_passo9._set_appearance_mode("dark")
        label_passo9.pack(pady=20)
        label_imagem9 = ctk.CTkLabel(abas2.tab("Passo 9"), image=imagem9, text="")  # Imagem do segundo passo.
        label_imagem9.pack(pady=0)

        label_passo10 = ctk.CTkLabel(abas2.tab("Passo 10"),  # Label com o terceiro passo.
                                    text="10. Decore como quiser.", font=("Arial", 22))
        label_passo10._set_appearance_mode("dark")
        label_passo10.pack(pady=20)
        label_imagem10 = ctk.CTkLabel(abas2.tab("Passo 10"), image=imagem10, text="")  # Imagem do terceiro passo.
        label_imagem10.pack(pady=0)

        label_passo11 = ctk.CTkLabel(abas2.tab("Passo 11"),  # Label com o quarto passo.
                                    text="11. Separe um tira de barbante e faça um nó em cada ponta.", font=("Arial", 22))
        label_passo11._set_appearance_mode("dark")
        label_passo11.pack(pady=20)
        label_imagem11 = ctk.CTkLabel(abas2.tab("Passo 11"), image=imagem11, text="")  # Imagem do quarto passo.
        label_imagem11.pack(pady=0)

        label_passo12 = ctk.CTkLabel(abas2.tab("Passo 12"),  # Label com o quinto passo.
                                    text="12. Logo após, insira um pedaço de algum material sintético como manta bidim ou TNT no meio do barbante.", font=("Arial", 22))
        label_passo12._set_appearance_mode("dark")
        label_passo12.pack(pady=20)
        label_imagem12 = ctk.CTkLabel(abas2.tab("Passo 12"), image=imagem12, text="")  # Imagem do quinto passo.
        label_imagem12.pack(pady=0)

        label_passo13 = ctk.CTkLabel(abas2.tab("Passo 13"),  # Label com o quinto passo.
                                    text="13. Acople a parte superior da garrafa de forma inversa, com o barbante atravessando o gargalo.",
                                    font=("Arial", 22))
        label_passo13._set_appearance_mode("dark")
        label_passo13.pack(pady=20)
        label_imagem13 = ctk.CTkLabel(abas2.tab("Passo 13"), image=imagem13, text="")  # Imagem do quinto passo.
        label_imagem13.pack(pady=0)

        label_passo14 = ctk.CTkLabel(abas2.tab("Passo 14"),  # Label com o quinto passo.
                                    text="14. Coloque terra e uma planta pequena com raiz.",
                                    font=("Arial", 22))
        label_passo14._set_appearance_mode("dark")
        label_passo14.pack(pady=20)
        label_imagem14 = ctk.CTkLabel(abas2.tab("Passo 14"), image=imagem14, text="")  # Imagem do quinto passo.
        label_imagem14.pack(pady=0)

        label_passo15 = ctk.CTkLabel(abas2.tab("Passo 15"),  # Label com o quinto passo.
                                     text="15. Por fim, coloque água na parte inferior da garrafa.",
                                     font=("Arial", 22))
        label_passo15._set_appearance_mode("dark")
        label_passo15.pack(pady=20)
        label_imagem15 = ctk.CTkLabel(abas2.tab("Passo 15"), image=imagem15, text="")  # Imagem do quinto passo.
        label_imagem15.pack(pady=0)
        label_passo15_obs = ctk.CTkLabel(abas2.tab("Passo 15"),  # Label com o quinto passo.
                                     text="OBS: Caso a parte de cima seja pintada, é interessante não deixar água entrar em contato com a tinta.",
                                     font=("Arial", 22), text_color="Grey")
        label_passo15_obs._set_appearance_mode("dark")
        label_passo15_obs.pack(pady=20)

        label_fonte = ctk.CTkLabel(frame_receita_vidro,  # Label da fonte da imagem
                                   text="Fonte: GavetaMix - Youtube. Disponível em: <https://youtu.be/EpWiENvkvTE>",
                                   font=("Arial", 25), text_color="Grey")
        label_fonte._set_appearance_mode("dark")
        label_fonte.pack(pady=20)

        label_espaco = ctk.CTkLabel(frame_receita_vidro, text="") # Label que cria um espaço na página.
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(side="bottom", pady=0)

        botao_fim = ctk.CTkButton(frame_receita_vidro, text="Fim", font=("Arial", 24), width=100,  # Botão que avança para a página final.
                                  height=40, text_color="White", fg_color="Red",
                                  command=lambda: fim_receita(frame_receita_vidro, janela, menu, menu_func, voltar_func))
        botao_fim._set_appearance_mode("dark")
        botao_fim.pack(side="bottom", pady=5)

        botao_receita_menu = ctk.CTkButton(frame_receita_vidro, text="Menu", font=("Arial", 24), width=100,  # Botão que volta ao menu inicial dentro da página temporária.
                                           height=40,
                                           command=lambda: menu_func(frame_receita_vidro, menu))
        botao_receita_menu._set_appearance_mode("dark")
        botao_receita_menu.pack(side="bottom", pady=5)

        botao_receita_voltar = ctk.CTkButton(frame_receita_vidro, text="Voltar", font=("Arial", 24), width=100,  # Botão que volta á pagina anterior dentro da página temporária.
                                             height=40,
                                             command=lambda: voltar_func(frame_receita_vidro, pagina))
        botao_receita_voltar._set_appearance_mode("dark")
        botao_receita_voltar.pack(side="bottom", pady=5)

    botao_receita = ctk.CTkButton(pagina, text="Vaso Auto Irrigavel com Garrafa de Vidro", command=receita, # Botão com o nome da receita que tem como comando a função receita().
                                  fg_color="#CED4DA", text_color="black", hover_color="#6C757D")
    botao_receita._set_appearance_mode("dark")

    return botao_receita # retorna o botão da receita.

def botao_receita_menor(pagina, janela, menu, menu_func, voltar_func): # função do botão da receita.

    def receita(): # função da pagina da receita.

        pagina.pack_forget() # "Esquece" a página anterior ou fecha a página anterior.

        frame_receita_vidro = ctk.CTkFrame(janela) # Cria uma nova página.
        frame_receita_vidro._set_appearance_mode("dark")
        frame_receita_vidro.pack(fill="both", expand=True)

        label_receita_vidro = ctk.CTkLabel(frame_receita_vidro,  # Label que fala a receita.
                                           text="Materiais: Garrafa de vidro, barbante, pincel, planta, cola e outros materiais para decoração.", font= ("Arial", 25))
        label_receita_vidro._set_appearance_mode("dark")
        label_receita_vidro.pack(pady=50)

        imagem1 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_1_vasov.jpeg"), size=(400, 300)) # Alocação de imagens a uma variável.
        imagem2 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_2_vasov.jpeg"), size=(400, 300))
        imagem3 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_3_vasov.jpeg"), size=(400, 300))
        imagem4 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_4_vasov.jpeg"), size=(400, 300))
        imagem5 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_5_vasov.jpeg"), size=(400, 300))
        imagem6 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_6_vasov.jpeg"), size=(400, 300))
        imagem7 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_7_vasov.jpeg"), size=(400, 300))

        abas = ctk.CTkTabview(frame_receita_vidro, segmented_button_fg_color="White", segmented_button_unselected_color="#CED4DA",  # criação de abas dentro da pagina.
                              segmented_button_unselected_hover_color="#CED4DA", segmented_button_selected_color="#6C757D", text_color="Black", segmented_button_selected_hover_color="#6C757D")
        abas._set_appearance_mode("dark")
        abas.pack(pady=0)

        abas.add("Passo 1") # Adicionando os nomes das abas.
        abas.add("Passo 2")
        abas.add("Passo 3")
        abas.add("Passo 4")
        abas.add("Passo 5")
        abas.add("Passo 6")
        abas.add("Passo 7")

        label_passo1 = ctk.CTkLabel(abas.tab("Passo 1"), # Label com o primeiro passo.
                                    text="1. Adicione cola na garrafa de vidro.", font=("Arial", 22))
        label_passo1._set_appearance_mode("dark")
        label_passo1.pack(pady=20)
        label_imagem1 = ctk.CTkLabel(abas.tab("Passo 1"), image=imagem1, text="") #Imagem do primeiro passo.
        label_imagem1.pack(pady=0)

        label_passo2 = ctk.CTkLabel(abas.tab("Passo 2"), # Label com o segundo passo.
                                    text="2. Espalhe a cola na garrafa com um pincel. ", font=("Arial", 22))
        label_passo2._set_appearance_mode("dark")
        label_passo2.pack(pady=20)
        label_imagem2 = ctk.CTkLabel(abas.tab("Passo 2"), image=imagem2, text="") # Imagem do segundo passo.
        label_imagem2.pack(pady=0)

        label_passo3 = ctk.CTkLabel(abas.tab("Passo 3"), # Label com o terceiro passo.
                                    text="3. A partir da base da garrafa, com um barbante de sua escolha, passe ao redor da garrafa.", font=("Arial", 22))
        label_passo3._set_appearance_mode("dark")
        label_passo3.pack(pady=20)
        label_imagem3 = ctk.CTkLabel(abas.tab("Passo 3"), image=imagem3, text="") # Imagem do terceiro passo.
        label_imagem3.pack(pady=0)

        label_passo4 = ctk.CTkLabel(abas.tab("Passo 4"), # Label com o quarto passo.
                                    text="4. Você pode personalizar com um diferentes cores e estilos de barbante de acordo com sua preferência.", font=("Arial", 22))
        label_passo4._set_appearance_mode("dark")
        label_passo4.pack(pady=20)
        label_imagem4 = ctk.CTkLabel(abas.tab("Passo 4"), image=imagem4, text="") # Imagem do quarto passo.
        label_imagem4.pack(pady=0)

        label_passo5 = ctk.CTkLabel(abas.tab("Passo 5"), # Label com o quinto passo.
                                    text="5. Apos passar o barbante até o topo da garrafa, retoque com cola para manter o barbante bem firmado.", font=("Arial", 22))
        label_passo5._set_appearance_mode("dark")
        label_passo5.pack(pady=20)
        label_imagem5 = ctk.CTkLabel(abas.tab("Passo 5"), image=imagem5, text="") # Imagem do quinto passo.
        label_imagem5.pack(pady=0)

        label_passo6 = ctk.CTkLabel(abas.tab("Passo 6"),  # Label com o sexto passo.
                                    text="6. Adicione detalhes de sua preferência para estilizar seu vaso de vidro.",
                                    font=("Arial", 22))
        label_passo6._set_appearance_mode("dark")
        label_passo6.pack(pady=20)
        label_imagem6 = ctk.CTkLabel(abas.tab("Passo 6"), image=imagem6, text="")  # Imagem do sexto passo.
        label_imagem6.pack(pady=0)

        label_passo7 = ctk.CTkLabel(abas.tab("Passo 7"),  # Label com o setimo passo.
                                    text="7. Aqui esta o exemplo de como sua garrafa de vidro pode ser transformada em vaso de vidro personalizado.",
                                    font=("Arial", 22))
        label_passo7._set_appearance_mode("dark")
        label_passo7.pack(pady=20)
        label_imagem7 = ctk.CTkLabel(abas.tab("Passo 7"), image=imagem7, text="")  # Imagem do setimo passo.
        label_imagem7.pack(pady=0)

        label_fonte = ctk.CTkLabel(frame_receita_vidro,  # Label da fonte da imagem
                                   text="Fonte: Maria Figueiredo DIY - Youtube. Disponível em: <https://youtu.be/6gFoatY7C0o>",
                                   font=("Arial", 25), text_color="Grey")
        label_fonte._set_appearance_mode("dark")
        label_fonte.pack(pady=20)

        label_espaco = ctk.CTkLabel(frame_receita_vidro, text="") # Label que cria um espaço na página.
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(side="bottom", pady=0)

        botao_fim = ctk.CTkButton(frame_receita_vidro, text="Fim", font=("Arial", 24), width=100,  # Botão que avança para a página final.
                                  height=40, text_color="White", fg_color="Red",
                                  command=lambda: fim_receita(frame_receita_vidro, janela, menu, menu_func, voltar_func))
        botao_fim._set_appearance_mode("dark")
        botao_fim.pack(side="bottom", pady=5)

        botao_receita_menu = ctk.CTkButton(frame_receita_vidro, text="Menu", font=("Arial", 24), width=100,  # Botão que volta ao menu inicial dentro da página temporária.
                                           height=40,
                                           command=lambda: menu_func(frame_receita_vidro, menu))
        botao_receita_menu._set_appearance_mode("dark")
        botao_receita_menu.pack(side="bottom", pady=5)

        botao_receita_voltar = ctk.CTkButton(frame_receita_vidro, text="Voltar", font=("Arial", 24), width=100,  # Botão que volta á pagina anterior dentro da página temporária.
                                             height=40,
                                             command=lambda: voltar_func(frame_receita_vidro, pagina))
        botao_receita_voltar._set_appearance_mode("dark")
        botao_receita_voltar.pack(side="bottom", pady=5)

    botao_receita = ctk.CTkButton(pagina, text="Vaso de Planta com Garrafa de Vidro", command=receita, # Botão com o nome da receita que tem como comando a função receita().
                                  fg_color="#CED4DA", text_color="black", hover_color="#6C757D")
    botao_receita._set_appearance_mode("dark")

    return botao_receita # retorna o botão da receita.
