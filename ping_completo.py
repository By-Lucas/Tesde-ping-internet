import functools
import os
import tkinter as tk
from concurrent import futures
from tkinter import ttk, messagebox, Tk, tix
import time
import sys


thread_pool_executor = futures.ThreadPoolExecutor(max_workers=1)

def tk_after(target):

    @functools.wraps(target)
    def wrapper(self, *args, **kwargs):
        args = (self,) + args
        self.after(0, target, *args, **kwargs)

    return wrapper

def submit_to_pool_executor(executor):

    def decorator(target):

        @functools.wraps(target)
        def wrapper(*args, **kwargs):
            return executor.submit(target, *args, **kwargs)

        return wrapper

    return decorator


class MainFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master.title('PING PYTHON ')
        self.master.configure(background='#0B3861') #Background da pagina
        self.master.geometry('800x520') # Tamanho da janela
        self.master.resizable(False, False) #Se pode aumentar e diminuir tamabnho da janela
        self.master.maxsize(width=2000, height=1000) #Tamanho maximo da tela
        self.master.minsize(width=600, height=500) #Tamanho minimo da tela

        
        self.caminho_ping = tk.Entry(self.master, font='Verdana 14')
        self.caminho_ping.place(x=150, y=30, height=40)
        self.caminho_ping.insert(-1,"8.8.8.8")

        self.label2 = tk.Label(self.master, bg='#0B3861' ,text='QUANTIDADE DE PING', fg='WHITE', font='Verdana 12')
        self.label2.place(x=400, y=40)

        self.quantidade_ping = tk.Entry(self.master, font='arial 14')
        self.quantidade_ping.place(x=600, y=30, height=40, width=40)
        self.quantidade_ping.insert(-1,"5")

        self.entry = tk.StringVar()

        entry = tk.Entry(self.master, textvariable=self.entry, font='Verdana 14')
        entry.insert(-1, "8.8.8.8")
        entry.place(x=150, y=30, height=40)

        self.button = tk.Button( self.master, text="Iniciar ping",command=self.ping , cursor='hand2' ,bg='green', fg='white', font='Verdana 12')
        self.button.place(x=20, y=20, width=100, height=50)

        self.parar_ = tk.Button( self.master, text="Logout",command=self.sair , cursor='hand2' ,bg='red', fg='white', font='Verdana 12')
        self.parar_.place(x=680, y=20, width=100, height=50)

        self.text = tk.Text(self.master,  font='Verdana 10', bg='silver')
        self.text.config(state=tk.DISABLED)
        self.text.place(x=78, y=100)

    @tk_after
    def button_state(self, enabled=True):
        state = tk.NORMAL
        if not enabled:
            state = tk.DISABLED
        self.button.config(state=state)

    @tk_after
    def clear_text(self):
        self.text.config(state=tk.NORMAL)
        self.text.delete(1.0, tk.END)
        self.text.config(state=tk.DISABLED)

    @tk_after
    def insert_text(self, text):
        self.text.config(state=tk.NORMAL)
        self.text.insert(tk.END, text)
        self.text.config(state=tk.DISABLED)
    
    def sair(self):
        res = messagebox.askquestion ('Sair do aplicativo', 'Você realmente deseja sair?')
        if res == 'yes':
            app.destroy()
        else :
            print('Retornar ao aplicativo principal')

    @submit_to_pool_executor(thread_pool_executor)
    def ping(self):
        self.button_state(False)
        self.clear_text()
        self.insert_text('CRIADO POR: LUCAS SILVA\n\nWHATSAPP = 74981199190\n\nINICIANDO PING\n')

        result = os.popen("ping "+self.entry.get()+" -n "+self.quantidade_ping.get())
        for line in result:
            self.insert_text(line)

        self.insert_text('PING TERMINADO')
        self.button_state(True)


if __name__ == '__main__':
    app = tk.Tk()
    main_frame = MainFrame()
    app.mainloop()