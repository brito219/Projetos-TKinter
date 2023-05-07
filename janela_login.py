import customtkinter

#janela de login bonitaa

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def click():
    print("Fazer Login")

win = customtkinter.CTk()
win.geometry("500x250")

texto = customtkinter.CTkLabel(win, text="Fazer Login.")

email = customtkinter.CTkEntry(win, placeholder_text="E-mail")

senha = customtkinter.CTkEntry(win, placeholder_text="Senha", show="*")

botao = customtkinter.CTkButton(win, text="Login", command=click)

texto.pack(padx=10, pady=10)
email.pack(padx=10, pady=10)
senha.pack(padx=10, pady=10)
botao.pack(padx=10, pady=10)

win.mainloop()
