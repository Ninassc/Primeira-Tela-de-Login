import customtkinter as ctk


ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')


janela = ctk.CTk()
janela.title('Login')
janela.geometry('500x300')


def clicar_botao():
    print("Button clicked!")  
    email = email_entry.get()
    senha = senha_entry.get()
    print("Email:", email)  
    print("Senha:", senha)  

    email_entry.delete(0, ctk.END)
    senha_entry.delete(0, ctk.END)


login = ctk.CTkLabel(janela, text='Faça seu login')
login.pack(padx=10, pady=10)

email_entry = ctk.CTkEntry(janela, placeholder_text='Email', height=30, width=200)
email_entry.pack(padx=10, pady=10)

senha_entry = ctk.CTkEntry(janela, placeholder_text='Senha', show='*', height=30, width=200)
senha_entry.pack(padx=10, pady=10)

checkbox = ctk.CTkCheckBox(janela, text='Lembre-me do login', height=0.5, width=0.5)
checkbox.pack(padx=10, pady=10)

botao = ctk.CTkButton(janela, text='Confirmar', command=clicar_botao)
botao.pack(padx=10, pady=10)


def direcionarJanela():
    novaJanela = ctk.CTkToplevel(janela, fg_color='teal')
    novaJanela.geometry('400x200')

botao2 = ctk.CTkButton(janela, text='Abrir Janela', command=direcionarJanela)
botao2.pack(padx=10)


janela.mainloop()
