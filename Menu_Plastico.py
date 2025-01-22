import customtkinter as ctk

def pag_plastico(janela, menu, plastico, tampa):
    pagina_plastico_escolha = ctk.CTkFrame(janela)
    pagina_plastico_escolha._set_appearance_mode("dark")
    label2 = ctk.CTkLabel(pagina_plastico_escolha, text="Escolha", font=("Arial", 24))
    label2._set_appearance_mode("dark")
    label2.pack(pady=50)
    botao_plastico = ctk.CTkButton(pagina_plastico_escolha, text="Plástico", command=plastico, fg_color="#A7C7E7", text_color="black", hover_color="#B0E0E6")
    botao_plastico._set_appearance_mode("dark")
    botao_plastico.pack(pady=20)
    botao_tampas = ctk.CTkButton(pagina_plastico_escolha, text="Tampa de Garrafa", command=tampa, fg_color="#A7C7E7", text_color="black", hover_color="#B0E0E6")
    botao_tampas._set_appearance_mode("dark")
    botao_tampas.pack(pady=20)
    botao_plastico_menu = ctk.CTkButton(pagina_plastico_escolha, text="Menu", font=("Arial", 24), width=100, height=40, command=menu)
    botao_plastico_menu._set_appearance_mode("dark")
    botao_plastico_menu.pack(side="bottom", pady=20)
    return pagina_plastico_escolha


def pag_plastico_escolha(janela, menu, voltar):
    pagina_plastico_e_ = ctk.CTkFrame(janela)
    pagina_plastico_e_._set_appearance_mode("dark")
    label_plastico = ctk.CTkLabel(pagina_plastico_e_, text="Plástico", font=("Arial", 24))
    label_plastico._set_appearance_mode("dark")
    label_plastico.pack(pady=50)
    botao_plastico_voltar = ctk.CTkButton(pagina_plastico_e_, text="Voltar", command=voltar)
    botao_plastico_voltar._set_appearance_mode("dark")
    botao_plastico_voltar.pack(pady=20)
    botao_plastico_e_menu = ctk.CTkButton(pagina_plastico_e_, text="Menu", command=menu)
    botao_plastico_e_menu._set_appearance_mode("dark")
    botao_plastico_e_menu.pack(pady=20)
    return pagina_plastico_e_


def pag_tampa(janela, menu, voltar):
    pagina_tampa = ctk.CTkFrame(janela)
    pagina_tampa._set_appearance_mode("dark")
    label_tampa = ctk.CTkLabel(pagina_tampa, text="Tampa de Garrafa", font=("Arial", 24))
    label_tampa._set_appearance_mode("dark")
    label_tampa.pack(pady=50)
    botao_tampa_voltar = ctk.CTkButton(pagina_tampa, text="Voltar", command=voltar)
    botao_tampa_voltar._set_appearance_mode("dark")
    botao_tampa_voltar.pack(pady=20)
    botao_tampa_menu = ctk.CTkButton(pagina_tampa, text="Menu", command=menu)
    botao_tampa_menu._set_appearance_mode("dark")
    botao_tampa_menu.pack(pady=20)
    return pagina_tampa