import customtkinter as ctk

def pag_descarte(janela, menu):
    pagina_descarte = ctk.CTkFrame(janela)
    pagina_descarte._set_appearance_mode("dark")
    label5 = ctk.CTkLabel(pagina_descarte, text="Descarte", font=("Arial", 24))
    label5._set_appearance_mode("dark")
    label5.pack(pady=50)
    botao_descarte2 = ctk.CTkButton(pagina_descarte, text="Menu", font=("Arial", 24), width=100, height=40, command=menu)
    botao_descarte2._set_appearance_mode("dark")
    botao_descarte2.pack(side="bottom", pady=20)
    return pagina_descarte