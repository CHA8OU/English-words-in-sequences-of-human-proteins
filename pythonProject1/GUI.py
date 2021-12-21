from tkinter import *
from words_in_proteome import *
from tkinter import messagebox


f = open("english-common-words.txt", "r")
fasta = open ("human-proteome.fasta","r")

list=read_words(f)
dict=read_sequences(fasta)
dict_occurrence=search_words_in_proteome(list,dict)
def button1_output():
    messagebox.showinfo("output:","TOTAL WORDS: "+str(len(list)))

def button2_output():
    messagebox.showinfo("output:","TOTAL SEQUENCES: "+str(len(dict)))

def button3_output():
    x=var.get()
    if(x in dict.keys()):
        messagebox.showinfo("output ",dict[x])
    else:
        messagebox.showinfo("output: ","Verifier votre saisie")

def button4_output():
    x=var.get()
    if x in dict_occurrence.keys():
        ch=str(x)+" FOUND IN "+str(dict_occurrence[x])+" SEQUENCES"
        messagebox.showinfo("output:",ch)
    else:
        messagebox.showinfo("output","Verifier votre saisie")


main=Tk()
main.title("Hire Now")
main.geometry("1024x600")
main.config(background='#FF0000')
my_title=Label(main,text="MINI_PROJET",font=("Courier New Baltic",60),bg='#FF0000')
my_title.pack()
frame1=Frame(main,bg='#FF0000')
L1=Label(frame1,text="Entrer une protéine :",font=20,bg='#FF0000')
L1.pack()
var=StringVar()
E1=Entry(frame1,textvariable=var,width=80)
E1.pack()
button2=Button(frame1,text="Total Words",command=button1_output)
button2.pack(padx=5,pady=5,fill=X)
button3=Button(frame1,text="Total Sequences",command=button2_output)
button3.pack(padx=5,pady=5,fill=X)
button1=Button(frame1,text="Read Sequence",command=button3_output)
button1.pack(padx=5,pady=5,fill=X)
button4=Button(frame1,text="Total Word In Sequence",command=button4_output)
button4.pack(padx=5,pady=5,fill=X)
frame1.pack()
main.mainloop()