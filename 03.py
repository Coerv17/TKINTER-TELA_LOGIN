import customtkinter as ctk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# janela.geometry("{0}x{1}+0+0".format(janela.winfo_screenwidth(), janela.winfo_screenheight()))

def clk():
    
    opt1 = Toplevel(janela)
    opt1.geometry("400x200+800+300")
    opt1.resizable(False, False)  
    opt1.iconbitmap("logo.ico")
    opt1.title("Top")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    janela.hide()
 
# janela
janela = ctk.CTk()
janela.geometry("300x400")
janela.title("sistema de login")
janela.iconbitmap("logocomal(certo).ico")
janela.resizable(False, False)
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("dark-blue")

botao = ctk.CTkButton(master=janela, text="clique aqui",command= clk)
botao.place(x=25, y=25)

janela.mainloop()


  def usu():
                username = username_entry.()
                email = email_entry()
                passw = pass_entry.get()
                Cpass= cPass_entry.get()
                database.cursor.execute('''
                INSERT INTO users(Username,Email,Senha,Confsenha(username,email,passw,Cpass)VALUES(?, ?, ?, ?))
                ''',(username, email, passw, Cpass))
                database.conn.commit()