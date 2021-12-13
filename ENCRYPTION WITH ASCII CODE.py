
from tkinter import *
root=Tk()
root.title("ENCRYPTION WITH ASCII CODE")
root.geometry("400x400")
textinput=Entry(root)
textinput.place(relx=0.5,rely=0.5,anchor=CENTER)
textlabel=Label(root,text="Name in Ascii: ")
textlabel2=Label(root,text="Encryted Name: ")

def AsciiConverter():
    name=textinput.get()
    for i in name:
        ascii=int(ord(i))
        encrypted=ascii+3
        textlabel["text"]+=str(ascii)+" "
        textlabel2["text"]+=str(chr(encrypted))
        
        
button1=Button(root,text="Convert", command=AsciiConverter)

button1.place(relx=0.5,rely=0.6,anchor=CENTER)
textlabel.place(relx=0.5,rely=0.7,anchor=CENTER)
textlabel2.place(relx=0.5,rely=0.8,anchor=CENTER)

root.mainloop()