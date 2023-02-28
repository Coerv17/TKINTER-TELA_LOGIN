import customtkinter as ctk
from tkinter import *
from tk inter import ttk


janela = ctk.CTk()


class Applicatiom():
	def __init__(self):
   self.janela = janela
   self.tema()
   self.tela()
   self.janela_login()
   janela.mainloop()
  
  def tema(self):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
  
  def tela(self):
    self.janela.geometry("700x400")
    self.janela.title("sistema de login")
    self.janela.iconbitmpa("icon.ico")
    self.janela.resizable(False, False)
  
  def tela_login(self):
    #imagem na tela
    img = PhotoImage(file="logocomal.png")
    label_img = ctk.CTklabel(master=janela, image=img)
    label_img.place(x=5, y=65)

    label_tt = ctk.CTkLabel(master=janela, text="Entre na sua conta e tenha\na plataforma",
    text_font=("Roboto",18), tex_color="#00B0F0").place(x=10, y=10)

    #frame
    login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
    login_frame.pack(side=RIGHT)

    #frame widgets
    label = ctk.CTkLabel(master=login_frame, text="Sistema de login", text_font("Roboto",20))
    label.place(x=25, y=5)

    username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Nome de usuario", width=300, text_font("Roboto",14)).place(x=25, y=5)

    username_label = ctk.CTklabel(master=login_frame, )
   
