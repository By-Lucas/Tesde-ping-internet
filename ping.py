import subprocess
import os
from tkinter import *
from tkinter import ttk, messagebox, Tk
from tkinter import scrolledtext


janela  = Tk()


class janela1():
    def __init__(self): 
        self.janela = janela

        self.tela_principal()

        janela.mainloop()
        
    #Tele principal
    def tela_principal(self):
        self.janela.title('PING PYTHON ')
        self.janela.configure(background='#0B3861') #Background da pagina
        self.janela.geometry('800x500') # Tamanho da janela
        self.janela.resizable(False, False) #Se pode aumentar e diminuir tamabnho da janela
        self.janela.maxsize(width=2000, height=1000) #Tamanho maximo da tela
        self.janela.minsize(width=600, height=500) #Tamanho minimo da tela
        
        self.pingar = Button(self.janela, text="Fazer ping",command=self.ping_test, cursor='hand2' ,bg='green', fg='white', font='arial 12')
        self.pingar.place(x=20, y=20, width=100, height=50)

        self.caminho_ping = Entry(self.janela, font='arial 12')
        self.caminho_ping.place(x=150, y=30, height=40)

        self.label1 = Label(self.janela, bg='yellow', text='RESULTADO PING', fg='green', font='arial 14')
        self.label1.place(x=250, y=400, width=250, height=60)



        self.textos = scrolledtext.ScrolledText(self.janela,width=50,height=10)
        #self.textos.insert(INSERT,'oi' )
        self.textos.place(x=200, y=100)

    def progres_bar(self):
        pb = ttk.Progressbar(self.janela, orient="horizontal", length=300,mode="determinate")
        pb.pack(side='bottom')
        self.label1['text'] = pb
        pb.start()
        
        
        
        

    def ping_test (self):
        hostname = self.caminho_ping.get()#"www.google.com" #example
        response = os.system(f"ping -n 10 {hostname}")
        
        self.label1["text"] = 'Percas', response

        #and then check the response...
        if response == 0:
            print (hostname, 'Esta para cima!')
            self.textos.insert(INSERT,'\nTotal de pecas: {} de {}'.format(response, hostname))
        else:
            print (hostname, 'Esta para baixo!')
            

janela1()