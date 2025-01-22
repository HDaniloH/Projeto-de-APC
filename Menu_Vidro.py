import customtkinter as ctk

def pag_vidro(janela, menu):
    pagina_vidro = ctk.CTkFrame(janela)
    pagina_vidro._set_appearance_mode("dark")
    label4 = ctk.CTkLabel(pagina_vidro, text="Vidro", font=("Arial", 24))
    label4._set_appearance_mode("dark")
    label4.pack(pady=50)
    botao_vidro2 = ctk.CTkButton(pagina_vidro, text="Menu", font=("Arial", 24), width=100, height=40, command=menu)
    botao_vidro2._set_appearance_mode("dark")
    botao_vidro2.pack(side="bottom", pady=20)
    return pagina_vidro