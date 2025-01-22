import customtkinter as ctk

def pag_papelao(janela, menu, papelao, caixa):
    pagina_papelao = ctk.CTkFrame(janela)
    pagina_papelao._set_appearance_mode("dark")
    label2 = ctk.CTkLabel(pagina_papelao, text="Escolha", font=("Arial", 24))
    label2._set_appearance_mode("dark")
    label2.pack(pady=50)
    botao_papelao = ctk.CTkButton(pagina_papelao, text="Papelão", command=papelao, fg_color="#8B4513", hover_color="#654321")
    botao_papelao._set_appearance_mode("dark")
    botao_papelao.pack(pady=20)
    botao_caixa_papelao = ctk.CTkButton(pagina_papelao, text="Caixa de Papelão", command=caixa, fg_color="#8B4513", hover_color="#654321")
    botao_caixa_papelao._set_appearance_mode("dark")
    botao_caixa_papelao.pack(pady=20)
    botao_papelao_menu = ctk.CTkButton(pagina_papelao, text="Menu", font=("Arial", 24), width=100, height=40, command=menu)
    botao_papelao_menu._set_appearance_mode("dark")
    botao_papelao_menu.pack(side="bottom", pady=20)
    return pagina_papelao

def pag_papelao_escolha(janela, menu, voltar):
    pagina_papelao_e_ = ctk.CTkFrame(janela)
    pagina_papelao_e_._set_appearance_mode("dark")
    label_papelao = ctk.CTkLabel(pagina_papelao_e_, text="Papelão", font=("Arial", 24))
    label_papelao._set_appearance_mode("dark")
    label_papelao.pack(pady=50)
    botao_papelao_voltar = ctk.CTkButton(pagina_papelao_e_, text="Voltar", command=voltar)
    botao_papelao_voltar._set_appearance_mode("dark")
    botao_papelao_voltar.pack(pady=20)
    botao_papelao_menu = ctk.CTkButton(pagina_papelao_e_, text="Menu", command=menu)
    botao_papelao_menu._set_appearance_mode("dark")
    botao_papelao_menu.pack(pady=20)
    return pagina_papelao_e_

def pag_caixa(janela, menu, voltar):
    pagina_caixa = ctk.CTkFrame(janela)
    pagina_caixa._set_appearance_mode("dark")
    label_caixa = ctk.CTkLabel(pagina_caixa, text="Caixa de Papelão", font=("Arial", 24))
    label_caixa._set_appearance_mode("dark")
    label_caixa.pack(pady=50)
    botao_caixa_voltar = ctk.CTkButton(pagina_caixa, text="Voltar", command=voltar)
    botao_caixa_voltar._set_appearance_mode("dark")
    botao_caixa_voltar.pack(pady=20)
    botao_caixa_menu = ctk.CTkButton(pagina_caixa, text="Menu", command=menu)
    botao_caixa_menu._set_appearance_mode("dark")
    botao_caixa_menu.pack(pady=20)
    return pagina_caixa