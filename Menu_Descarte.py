import customtkinter as ctk
from PIL import Image, ImageTk
from receitas_plastico import fechar, fim_receita

def voltar_func(atual, anterior): # Função para voltar a pagina anterior dentro nas paginas temporarias do def
    atual.pack_forget()
    anterior.pack(fill="both", expand=True)

def menu_func(atual, menu): # Função para voltar ao menu dentro nas paginas temporarias do def
    atual.pack_forget()
    botao_menu_final = ctk.CTkButton(atual, text="Menu", command=menu())

def pag_descarte(janela, menu): # Função da pagina do descarte.

    pagina_descarte = ctk.CTkFrame(janela) # Cria a página do descarte.
    pagina_descarte._set_appearance_mode("dark")

    label = ctk.CTkLabel(pagina_descarte, text="Descarte", font=("Arial", 24)) # Label do descarte.
    label._set_appearance_mode("dark")
    label.pack(pady=50)

    label_descarte = ctk.CTkLabel(pagina_descarte, text="Como realizar o descarte de forma correta:", font=("Arial", 25)) # Label sobre como realizar o descarte de forma correta.
    label_descarte._set_appearance_mode("dark")
    label_descarte.pack(pady=10)

    imagem1 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_1_descarte.png"),size=(1000, 600)) # Alocação de imagens a uma variável.
    imagem2 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_2_descarte.png"),size=(1000, 600))
    imagem3 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_3_descarte.png"),size=(1000, 600))
    imagem4 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_4_descarte.png"),size=(1000, 600))
    imagem5 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_5_descarte.png"),size=(1000, 600))
    imagem6 = ctk.CTkImage(light_image=Image.open("Imagens receita/passo_6_descarte.png"),size=(1000, 600))


    abas = ctk.CTkTabview(pagina_descarte, segmented_button_fg_color="White") # Criação da aba.
    abas._set_appearance_mode("dark")
    abas.pack(pady=10)

    abas.add("Passo 1") # Criação de seções nas aba.
    abas.add("Passo 2")
    abas.add("Passo 3")
    abas.add("Passo 4")
    abas.add("Passo 5")
    abas.add("Passo 6")

    label_imagem1 = ctk.CTkLabel(abas.tab("Passo 1"), image=imagem1, text="")  # Imagem do primeiro passo.
    label_imagem1.pack(pady=25)

    label_imagem2 = ctk.CTkLabel(abas.tab("Passo 2"), image=imagem2, text="")  # Imagem do segundo passo.
    label_imagem2.pack(pady=25)

    label_imagem3 = ctk.CTkLabel(abas.tab("Passo 3"), image=imagem3, text="")  # Imagem do terceiro passo.
    label_imagem3.pack(pady=25)

    label_imagem4 = ctk.CTkLabel(abas.tab("Passo 4"), image=imagem4, text="")  # Imagem do quarto passo.
    label_imagem4.pack(pady=25)

    label_imagem5 = ctk.CTkLabel(abas.tab("Passo 5"), image=imagem5, text="")  # Imagem do quinto passo.
    label_imagem5.pack(pady=25)

    label_imagem6 = ctk.CTkLabel(abas.tab("Passo 6"), image=imagem6, text="")  # Imagem do sexto passo.
    label_imagem6.pack(pady=25)

    botao_fim = ctk.CTkButton(pagina_descarte, text="Fim", font=("Arial", 24), width=100, # Botão que avança para a página final.
                              height=40, text_color="White", fg_color="Red",
                              command=lambda: fim_receita(pagina_descarte, janela, menu, menu_func,
                                                          voltar_func))
    botao_fim._set_appearance_mode("dark")
    botao_fim.pack(side="bottom", pady=5)

    botao_descarte_menu = ctk.CTkButton(pagina_descarte, text="Menu", font=("Arial", 24), width=100, height=40, command=menu) # Botão que retorna ao menu incial.
    botao_descarte_menu._set_appearance_mode("dark")
    botao_descarte_menu.pack(side="bottom", pady=0)

    return pagina_descarte