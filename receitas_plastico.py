import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk

def fechar():
    exit()

def fim_receita(pagina_receita, janela, menu, menu_func, voltar_func): # função da pagina final.

    pagina_receita.pack_forget()

    pagina_final = ctk.CTkFrame(janela)  # Cria uma nova página.
    pagina_final._set_appearance_mode("dark")
    pagina_final.pack(fill="both", expand=True)

    label_espaco = ctk.CTkLabel(pagina_final,  # Label de espaço na pagina final
                               text="")
    label_espaco._set_appearance_mode("dark")
    label_espaco.pack(pady=50)

    label_final = ctk.CTkLabel(pagina_final,  # Label final 1
                               text="Chegamos ao fim..",
                               font=("Arial", 40))
    label_final._set_appearance_mode("dark")
    label_final.pack(pady=10)

    label_final2 = ctk.CTkLabel(pagina_final,  # Label final 2
                               text="Obrigado por ter usado o nosso programa!",
                               font=("Arial", 30))
    label_final2._set_appearance_mode("dark")
    label_final2.pack(pady=10)

    label_final3 = ctk.CTkLabel(pagina_final,  # Label final 3
                                text="Com isso, você está ajudando não só a si mesmo,",
                                font=("Arial", 30))
    label_final3._set_appearance_mode("dark")
    label_final3.pack(pady=10)

    label_final4 = ctk.CTkLabel(pagina_final,  # Label final 4
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

        frame_receita_garrafa_pet = ctk.CTkFrame(janela) # Cria uma nova página.
        frame_receita_garrafa_pet._set_appearance_mode("dark")
        frame_receita_garrafa_pet.pack(fill="both", expand=True)

        label_receita_garrafa_pet = ctk.CTkLabel(frame_receita_garrafa_pet, # Label que fala a receita.
                                                 text="Materiais: Garrafa pet, tinta, tesoura ou estilete, caneta para marcação", font= ("Arial", 25))
        label_receita_garrafa_pet._set_appearance_mode("dark")
        label_receita_garrafa_pet.pack(pady=50)

        imagem1 = ctk.CTkImage(light_image=Image.open("Imagens receita/Vasinhos de Plantas com Garrafa Pet 1.jpeg"), size=(300, 200)) # Alocação de imagens a uma variável.
        imagem2 = ctk.CTkImage(light_image=Image.open("Imagens receita/Vasinhos de Plantas com Garrafa Pet 2.jpeg"), size=(300, 200))
        imagem3 = ctk.CTkImage(light_image=Image.open("Imagens receita/Vasinhos de Plantas com Garrafa Pet 3.jpeg"), size=(300, 200))
        imagem4 = ctk.CTkImage(light_image=Image.open("Imagens receita/Vasinhos de Plantas com Garrafa Pet 4.jpeg"), size=(300, 200))
        imagem5 = ctk.CTkImage(light_image=Image.open("Imagens receita/Vasinhos de Plantas com Garrafa Pet 5.jpeg"), size=(300, 200))

        abas = ctk.CTkTabview(frame_receita_garrafa_pet, segmented_button_fg_color="White", segmented_button_unselected_color="#A7C7E7", # criação de abas dentro da pagina.
                              segmented_button_unselected_hover_color="#A7C7E7", segmented_button_selected_color="#B0E0E6", text_color="Black", segmented_button_selected_hover_color="#B0E0E6")
        abas._set_appearance_mode("dark")
        abas.pack(pady=0)

        abas.add("Passo 1") # Adicionando os nomes das abas.
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

        label_fonte = ctk.CTkLabel(frame_receita_garrafa_pet, # Label da fonte da imagem
                                   text="Fonte: Tata Pereira - Youtube.",
                                   font=("Arial", 25), text_color="Grey")
        label_fonte._set_appearance_mode("dark")
        label_fonte.pack(pady=20)

        label_espaco = ctk.CTkLabel(frame_receita_garrafa_pet, text="") # Label que cria um espaço na página.
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(side="bottom", pady=0)

        botao_fim = ctk.CTkButton(frame_receita_garrafa_pet, text="Fim", font=("Arial", 24), width=100, # Botão que avança para a página final.
                                  height=40, text_color="White", fg_color="Red",
                                  command=lambda: fim_receita(frame_receita_garrafa_pet, janela, menu, menu_func, voltar_func))
        botao_fim._set_appearance_mode("dark")
        botao_fim.pack(side="bottom", pady=5)

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

        label_receita_garrafa_pet = ctk.CTkLabel(frame_receita_garrafa_pet, # Label que fala a receita.
                                                 text="Materiais: Duas garrafas PET, um estilete (ou tesoura) e um marcador.", font= ("Arial", 25))
        label_receita_garrafa_pet._set_appearance_mode("dark")
        label_receita_garrafa_pet.pack(pady=50)

        imagem1 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_1_distribuidor.jpeg"), size=(300, 200)) # Alocação de imagens a uma variável.
        imagem2 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_2_distribuidor.jpeg"), size=(300, 200))
        imagem3 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_3_distribuidor.jpeg"), size=(300, 200))
        imagem4 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_4_distribuidor.jpeg"), size=(300, 200))
        imagem5 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_5_distribuidor.jpeg"), size=(300, 200))
        imagem6 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_6_distribuidor.jpeg"), size=(300, 200))
        imagem7 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_7_distribuidor.jpeg"), size=(300, 200))
        imagem8 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_8_distribuidor.jpeg"), size=(300, 200))

        abas = ctk.CTkTabview(frame_receita_garrafa_pet, segmented_button_fg_color="White", segmented_button_unselected_color="#A7C7E7", # criação de abas dentro da pagina.
                              segmented_button_unselected_hover_color="#A7C7E7", segmented_button_selected_color="#B0E0E6", segmented_button_selected_hover_color="#B0E0E6", text_color="Black")
        abas._set_appearance_mode("dark")
        abas.pack(pady=0)

        abas.add("Passo 1")
        abas.add("Passo 2")
        abas.add("Passo 3")
        abas.add("Passo 4")
        abas.add("Passo 5")
        abas.add("Passo 6")
        abas.add("Passo 7")
        abas.add("Passo 8")

        label_passo1 = ctk.CTkLabel(abas.tab("Passo 1"), # Label com o primeiro passo.
                                    text="1. Marque com a caneta a parte que será a vasilha onde o gato irá comer", font=("Arial", 22))
        label_passo1._set_appearance_mode("dark")
        label_passo1.pack(pady=20)
        label_imagem1 = ctk.CTkLabel(abas.tab("Passo 1"), image=imagem1, text="")  # Imagem do primeiro passo.
        label_imagem1.pack(pady=0)

        label_passo2 = ctk.CTkLabel(abas.tab("Passo 2"),  # Label com o segundo passo.
                                    text="2. Recorte com tesoura ou estilete.", font=("Arial", 22))
        label_passo2._set_appearance_mode("dark")
        label_passo2.pack(pady=20)
        label_imagem2 = ctk.CTkLabel(abas.tab("Passo 2"), image=imagem2, text="")  # Imagem do segundo passo.
        label_imagem2.pack(pady=0)

        label_passo3 = ctk.CTkLabel(abas.tab("Passo 3"),  # Label com o terceiro passo.
                                    text="3. Corte a garrafa que servirá de dispenser ao meio.", font=("Arial", 22))
        label_passo3._set_appearance_mode("dark")
        label_passo3.pack(pady=20)
        label_imagem3 = ctk.CTkLabel(abas.tab("Passo 3"), image=imagem3, text="")  # Imagem do terceiro passo.
        label_imagem3.pack(pady=0)

        label_passo4 = ctk.CTkLabel(abas.tab("Passo 4"),  # Label com o quarto passo.
                                    text="4. Corte na garrafa que servirá de vasilha um buraco do tamanho da boca da garrafa.", font=("Arial", 22))
        label_passo4._set_appearance_mode("dark")
        label_passo4.pack(pady=20)
        label_imagem4 = ctk.CTkLabel(abas.tab("Passo 4"), image=imagem4, text="")  # Imagem do quarto passo.
        label_imagem4.pack(pady=0)

        label_passo5 = ctk.CTkLabel(abas.tab("Passo 5"),  # Label com o quinto passo.
                                    text="5. Cole com cola quente uma garrafa na outra.", font=("Arial", 22))
        label_passo5._set_appearance_mode("dark")
        label_passo5.pack(pady=20)
        label_imagem5 = ctk.CTkLabel(abas.tab("Passo 5"), image=imagem5, text="")  # Imagem do quinto passo.
        label_imagem5.pack(pady=0)

        label_passo6 = ctk.CTkLabel(abas.tab("Passo 6"),  # Label com o sexto passo.
                                    text="6. Cole as tampinhas na base da garrafa.", font=("Arial", 22))
        label_passo6._set_appearance_mode("dark")
        label_passo6.pack(pady=20)
        label_imagem6 = ctk.CTkLabel(abas.tab("Passo 6"), image=imagem6, text="")  # Imagem do sexto passo.
        label_imagem6.pack(pady=0)

        label_passo7 = ctk.CTkLabel(abas.tab("Passo 7"),  # Label com o setimo passo.
                                    text="7. Coloque a ração no dispenser e tampe com o fundo da garrafa.", font=("Arial", 22))
        label_passo7._set_appearance_mode("dark")
        label_passo7.pack(pady=20)
        label_imagem7 = ctk.CTkLabel(abas.tab("Passo 7"), image=imagem7, text="")  # Imagem do setimo passo.
        label_imagem7.pack(pady=0)

        label_passo8 = ctk.CTkLabel(abas.tab("Passo 8"),  # Label com o oitavo passo.
                                    text="8. Agora você tem um dispenser de ração automático.", font=("Arial", 22))
        label_passo8._set_appearance_mode("dark")
        label_passo8.pack(pady=20)
        label_imagem8 = ctk.CTkLabel(abas.tab("Passo 8"), image=imagem8, text="")  # Imagem do oitavo passo.
        label_imagem8.pack(pady=0)

        label_fonte = ctk.CTkLabel(frame_receita_garrafa_pet,  # Label da fonte da imagem
                                   text="Fonte: Simple Ideas - Youtube. Disponível em: <https://youtu.be/PyvrU2e4IDg>",
                                   font=("Arial", 25), text_color="Grey")
        label_fonte._set_appearance_mode("dark")
        label_fonte.pack(pady=20)

        label_espaco = ctk.CTkLabel(frame_receita_garrafa_pet, text="")
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(side="bottom", pady=0)

        botao_fim = ctk.CTkButton(frame_receita_garrafa_pet, text="Fim", font=("Arial", 24), width=100, # Botão que avança para a página final.
                                  height=40, text_color="White", fg_color="Red",
                                  command=lambda: fim_receita(frame_receita_garrafa_pet, janela, menu, menu_func,voltar_func))
        botao_fim._set_appearance_mode("dark")
        botao_fim.pack(side="bottom", pady=5)

        botao_receita_menu = ctk.CTkButton(frame_receita_garrafa_pet, text="Menu", font=("Arial", 24), width=100,
                                           height=40,
                                           command=lambda: menu_func(frame_receita_garrafa_pet, menu))
        botao_receita_menu._set_appearance_mode("dark")
        botao_receita_menu.pack(side="bottom", pady=5)

        botao_receita_voltar = ctk.CTkButton(frame_receita_garrafa_pet, text="Voltar", font=("Arial", 24), width=100,
                                             height=40,
                                             command=lambda: voltar_func(frame_receita_garrafa_pet, pagina))
        botao_receita_voltar._set_appearance_mode("dark")
        botao_receita_voltar.pack(side="bottom", pady=5)

    botao_receita2 = ctk.CTkButton(pagina, text="Distribuidor caseiro de comida para animais de estimação", command=receita, fg_color="#A7C7E7", text_color="black",
                                   hover_color="#B0E0E6")
    botao_receita2._set_appearance_mode("dark")
    return botao_receita2

def botao_receita3(pagina, janela, menu, menu_func, voltar_func): # função do botão da receita.

    def receita(): # função da pagina da receita.

        pagina.pack_forget() # "Esquece" a página anterior ou fecha a página anterior.

        frame_receita_garrafa_pet = ctk.CTkFrame(janela) # Cria uma nova página.
        frame_receita_garrafa_pet._set_appearance_mode("dark")
        frame_receita_garrafa_pet.pack(fill="both", expand=True)

        label_receita_garrafa_pet = ctk.CTkLabel(frame_receita_garrafa_pet, # Label que fala a receita.
                                                 text="Materiais: Pelo menos 5 Garrafas PET, tesoura, barbante, pedriscos, substrato e a muda de hortaliça ou tempero desejado.", font= ("Arial", 25))
        label_receita_garrafa_pet._set_appearance_mode("dark")
        label_receita_garrafa_pet.pack(pady=50)

        imagem1 = ctk.CTkImage(light_image=Image.open("Imagens receita/parte_1_horta.png"), size=(300, 200)) # Alocação de imagens a uma variável.
        imagem2 = ctk.CTkImage(light_image=Image.open("Imagens receita/parte_2_horta.png"), size=(300, 200))

        abas = ctk.CTkTabview(frame_receita_garrafa_pet, segmented_button_fg_color="White", segmented_button_unselected_color="#A7C7E7", # criação de abas dentro da pagina.
                              segmented_button_unselected_hover_color="#A7C7E7", segmented_button_selected_color="#B0E0E6", text_color="Black", segmented_button_selected_hover_color="#B0E0E6")
        abas._set_appearance_mode("dark")
        abas.pack(pady=0)

        abas.add("Passo 1") # Adicionando os nomes das abas.
        abas.add("Passo 2")
        abas.add("Passo 3")
        abas.add("Passo 4")
        abas.add("Passo 5")
        abas.add("Passo 6")

        label_passo1 = ctk.CTkLabel(abas.tab("Passo 1"), # Label com o primeiro passo.
                                    text="1. Separe ao menos 5 garrafas PET para montar sua horta vertical.", font=("Arial", 22))
        label_passo1._set_appearance_mode("dark")
        label_passo1.pack(pady=20)
        label_imagem1 = ctk.CTkLabel(abas.tab("Passo 1"), image=imagem1, text="") #Imagem do primeiro passo.
        label_imagem1.pack(pady=0)

        label_passo2 = ctk.CTkLabel(abas.tab("Passo 2"), # Label com o segundo passo.
                                    text="2. Pegue uma das garrafas PET e corte com uma tesoura um pedaço na parte superior da garrafa.", font=("Arial", 22))
        label_passo2._set_appearance_mode("dark")
        label_passo2.pack(pady=20)
        label_imagem2 = ctk.CTkLabel(abas.tab("Passo 2"), image=imagem1, text="") # Imagem do segundo passo.
        label_imagem2.pack(pady=0)

        label_passo3 = ctk.CTkLabel(abas.tab("Passo 3"), # Label com o terceiro passo.
                                    text="3. Depois faça quatros furos principais (dois na parte superior e dois na parte inferior por onde irá passar o fio de metal ou barbante).", font=("Arial", 22))
        label_passo3._set_appearance_mode("dark")
        label_passo3.pack(pady=20)
        label_imagem3 = ctk.CTkLabel(abas.tab("Passo 3"), image=imagem1, text="") # Imagem do terceiro passo.
        label_imagem3.pack(pady=0)

        label_passo4 = ctk.CTkLabel(abas.tab("Passo 4"), # Label com o quarto passo.
                                    text="4. Seguidamente, faça micro furos na parte inferior da garrafa PET para que água acumulada possa escoar.", font=("Arial", 22))
        label_passo4._set_appearance_mode("dark")
        label_passo4.pack(pady=20)
        label_imagem4 = ctk.CTkLabel(abas.tab("Passo 4"), image=imagem1, text="") # Imagem do quarto passo.
        label_imagem4.pack(pady=0)

        label_passo5 = ctk.CTkLabel(abas.tab("Passo 5"), # Label com o quinto passo.
                                    text="5. Passe os fios de barbante ou corda entre os 4 buraquinhos das garrafas e faça nós para que elas fiquem sustentadas.", font=("Arial", 22))
        label_passo5._set_appearance_mode("dark")
        label_passo5.pack(pady=20)
        label_imagem5 = ctk.CTkLabel(abas.tab("Passo 5"), image=imagem1, text="") # Imagem do quinto passo.
        label_imagem5.pack(pady=0)

        label_passo6 = ctk.CTkLabel(abas.tab("Passo 6"),  # Label com o quinto passo.
                                    text="6. Por fim, com a estrutura já montada, acrescente pedriscos, o substrato e a muda de hortaliça ou tempero desejado.",
                                    font=("Arial", 22))
        label_passo6._set_appearance_mode("dark")
        label_passo6.pack(pady=20)
        label_passo6_1 = ctk.CTkLabel(abas.tab("Passo 6"),  # Label com o quinto passo.
                                    text="6.1. Regue as mudinhas sutilmente evitando que o substrato fique encharcado.",
                                    font=("Arial", 22))
        label_passo6_1._set_appearance_mode("dark")
        label_passo6_1.pack(pady=0)
        label_imagem6 = ctk.CTkLabel(abas.tab("Passo 6"), image=imagem2, text="")  # Imagem do quinto passo.
        label_imagem6.pack(pady=20)

        label_fonte = ctk.CTkLabel(frame_receita_garrafa_pet, # Label da fonte da imagem
                                   text="Fonte: Marcelo Rosenbaum.",
                                   font=("Arial", 25), text_color="Grey")
        label_fonte._set_appearance_mode("dark")
        label_fonte.pack(pady=20)

        label_espaco = ctk.CTkLabel(frame_receita_garrafa_pet, text="") # Label que cria um espaço na página.
        label_espaco._set_appearance_mode("dark")
        label_espaco.pack(side="bottom", pady=0)

        botao_fim = ctk.CTkButton(frame_receita_garrafa_pet, text="Fim", font=("Arial", 24), width=100, # Botão que avança para a página final.
                                  height=40, text_color="White", fg_color="Red",
                                  command=lambda: fim_receita(frame_receita_garrafa_pet, janela, menu, menu_func, voltar_func))
        botao_fim._set_appearance_mode("dark")
        botao_fim.pack(side="bottom", pady=5)

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

    botao_receita3 = ctk.CTkButton(pagina, text="Horta vertical com Garrafas PET", command=receita, # Botão com o nome da receita que tem como comando a função receita().
                                  fg_color="#A7C7E7", text_color="black", hover_color="#B0E0E6")
    botao_receita3._set_appearance_mode("dark")

    return botao_receita3 # retorna o botão da receita.