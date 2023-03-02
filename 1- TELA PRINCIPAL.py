import customtkinter as ctk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database


janela = ctk.CTk()

def ok ():
    # janela.destroy()
    top = ctk.CTkToplevel(janela)
    top.title("texto")
    top.geometry("800x600")
    top.iconbitmap("logo.ico")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    top.mainloop


    


class Applicatiom():
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()
  
    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
  
    def tela(self):
        self.janela.geometry("700x400")
        self.janela.title("sistema de login")
        self.janela.iconbitmap("logocomal(certo).ico")
        self.janela.resizable(False, False)
        
        
  
    def tela_login(self):
        #imagem na tela
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
        

        # def login ():
            
        #     msg= messagebox.showinfo(title="Estado de ",message="Parabens! Login feito com sucesso.")
        #     pass

        login_button = ctk.CTkButton(master=login_frame, text="LOGIN",width=300,command=ok).place(x=25, y=285)

        resgister_span= ctk.CTkLabel(master=login_frame, text="Não tem conta?").place(x=25, y=325)

        def tela_register():
            #removendo o frame de login
            login_frame.pack_forget()
            #criando a tela de cadastro de usuarios
            rg_frame = ctk.CTkFrame(master=janela, width=350, height=396)
            rg_frame.pack(side=RIGHT)
            
            label = ctk.CTkLabel(master=rg_frame, text= "FACA O SEU CADASTRO", font=("Centry Gothic bold",20)).place(x=25, y=5)
            span = ctk.CTkLabel(master=rg_frame, text="Por favor preencha todos os campos corretos.",font=("Centry Gothic bold",10),text_color="gray").place(x=25, y=65)
            
            username_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Nome de usuario", width=300, font=("Centry Gothic bold",14)).place(x=25, y=105)
            email_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="E-mail de usuario", width=300, font=("Centry Gothic bold",14)).place(x=25, y=145)
            pass_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Senha do usuario", width=300, font=("Centry Gothic bold",14),show="*").place(x=25, y=185)
            cPass_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Confirma senha", width=300, font=("Centry Gothic bold",14),show="*").place(x=25, y=225)
            checkbox = ctk.CTkCheckBox(master=rg_frame, text="Aceito dos termos e Politicas").place(x=25, y=265)
            def usu():
                username = username_entry.get()
                email = email_entry.get()
                passw = pass_entry.get()
                Cpass= cPass_entry.get()
                database.cursor.execute('''
                INSERT INTO users(Username,Email,Senha,Confsenha(username,email,passw,Cpass)VALUES(?, ?, ?, ?))
                ''',(username, email, passw, Cpass))
                database.conn.commit()

            
        
            def back():
                #removendo frame de cadastro
                rg_frame.pack_forget()

                #Devolvendo o frame de login
                login_frame.pack(side=RIGHT)


            back_button = ctk.CTkButton(master=rg_frame, text="VOLTAR",width=145,fg_color="gray",hover_color="#202020", command=back).place(x=25, y=300)
            
            def save_user():
                msg = messagebox.showinfo(title="Estado do Cadastro", message="Parabens! Usuario cadastrado com sucesso.")
                
                pass
            save_button = ctk.CTkButton(master=rg_frame, text="CADASTRAR",width=145,fg_color="green",hover_color="#014B05",command= usu).place(x=180, y=300)



            pass
        register_button = ctk.CTkButton(master=login_frame, text="CADASTRAR",width=150,
        fg_color="green", hover_color="#2D9334", command=tela_register).place(x=150, y=325)

    


Applicatiom()       

    
