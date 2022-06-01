from ast import Num, Pass
from cProfile import label
from cgi import test
from cgitb import text
from email import message
from logging import PlaceHolder
from os import access
from ssl import VerifyFlags
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter.tix import ButtonBox
from tokenize import Number
from turtle import bgcolor, color, left, title, width
from tkinter import ttk
from typing_extensions import Self
from django.db import DatabaseError
from numpy import place
from pyrsistent import b
from setuptools import Command
from zmq import EVENT_LISTENING
import tkinter as tk
from tkinter.tix import Select
import mysql.connector 

def consulta():
    tv = ttk.Treeview(jan,columns=('id', 'nome', 'fone' ), show='headings')
    tv.column('id', minwidth=0, width=100)
    tv.column('nome', minwidth=0,width=100)
    tv.column('fone', minwidth=0,width=100)
    tv.heading('id',text='CEP')
    tv.heading('nome',text='RUA')
    tv.heading('fone',text='BAIRRO')
    tv.place(x=200, y=180)

    consulta_sql =  "SELECT CEP, DESCRICAO, DESCRICAO_BAIRRO, UF, DESCRICAO_CIDADE from LOGRADOURO where CEP like '%"+PassEntry.get()+"%' AND UF LIKE '%RJ%'"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    tv.delete(*tv.get_children())
    for x in linhas: 
        tv.insert("","end",values=x)


jan = Tk()
jan.title('Acess Panel')
jan.geometry('700x500')
jan.configure(background="#ADD8E6")
jan.resizable(width=FALSE, height=FALSE) #Não consegue aumentar nem diminuir a tela

con = mysql.connector.connect( 
                     host = "localhost", 
                     user = "root", 
                     passwd = "", 
                     database = "MEUCEP" )  
cursorObject = con.cursor()  

#---------------Widgets--------------------
RightFrame = Frame(jan, width=700, height=50, bg="#363636", relief="raise")
RightFrame.pack(side=TOP)

TitleLabel = Label(jan, text='BUSCAR ENDEREÇO', font=('IMPACT', 20), foreground='white', background='#363636')
TitleLabel.place(x=252,y=5)

PassEntry = ttk.Entry(jan, width=60)
PassEntry.place(x=170, y=150)



CepButton = tk.Button(jan, text="BUSCAR", width=10, pady=1, bg="#363636", fg='white', command=consulta)
CepButton.place(x=560, y=148)

tv=ttk.Treeview(jan, columns=(''))

jan.mainloop()