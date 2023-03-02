#importar as bibliotecas
import customtkinter as ctk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox



# janela
janela = ctk.CTk()
janela.geometry("700x400")
janela.title("sistema de login")
janela.iconbitmap("logocomal(certo).ico")
janela.resizable(False, False)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#tela
img = PhotoImage(file="teste.png")
label_img = ctk.CTkLabel(master=janela, image=img, text="")
label_img.place(x=5, y=65)

label_tt = ctk.CTkLabel(master=janela, text="Entre na sua conta e tenha plataforma",font=("Centry Gothic bold",18),).place(x=10, y=10)

#frame
login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
login_frame.pack(side=RIGHT)
#frame widgets
label = ctk.CTkLabel(master=login_frame, text="Sistema de login", font=("Centry Gothic bold",20))
label.place(x=25, y=5)

username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Nome de usuario", width=300, font=("Centry Gothic bold",14)).place(x=25, y=105)
username_label = ctk.CTkLabel(master=login_frame,text="*O campo nome de usuario e de caracter e obrigatorio.",font=("Centry Gothic bold",8)).place(x=25, y=135)

password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="senha de usuario", width=300, font=("Centry Gothic bold",8), show="*").place(x=25, y=175)
passowor_label = ctk.CTkLabel(master=login_frame,text="*O campo nome de usuario e de caracter e obrigatorio.",font=("Centry Gothic bold",8)).place(x=25, y=205)

checkbox= ctk.CTkCheckBox(master=login_frame, text="Lembra-se de mim sempre").place(x=25, y=235)

login_button = ctk.CTkButton(master=login_frame, text="LOGIN",width=300).place(x=25, y=285)

resgister_span= ctk.CTkLabel(master=login_frame, text="Não tem conta?").place(x=25, y=325)

 #removendo o frame de login

login_frame.pack_forget()
# #criando a tela de cadastro de usuarios
# rg_frame = ctk.CTkFrame(master=janela, width=350, height=396)
# rg_frame.pack(side=RIGHT)

# label = ctk.CTkLabel(master=rg_frame, text= "FACA O SEU CADASTRO", font=("Centry Gothic bold",20)).place(x=25, y=5)
# span = ctk.CTkLabel(master=rg_frame, text="Por favor preencha todos os campos corretos.",font=("Centry Gothic bold",10),text_color="gray").place(x=25, y=65)

# username_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Nome de usuario", width=300, font=("Centry Gothic bold",14)).place(x=25, y=105)
# email_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="E-mail de usuario", width=300, font=("Centry Gothic bold",14)).place(x=25, y=145)
# pass_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Senha do usuario", width=300, font=("Centry Gothic bold",14),show="*").place(x=25, y=185)
# cPass_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Confirma senha", width=300, font=("Centry Gothic bold",14),show="*").place(x=25, y=225)
# checkbox = ctk.CTkCheckBox(master=rg_frame, text="Aceito dos termos e Politicas").place(x=25, y=265)




janela.mainloop()


