

from Tkinter import *
import ttk
import tkMessageBox
import urllib

root = Tk()
root.geometry("400x300")

link = "http://www.koeri.boun.edu.tr/scripts/lst9.asp"

kaynak = urllib.urlopen(link).readlines()

data = [{"bolge":data[8:], "tarih":data[0],
"saat":data[1], "enlem":data[2], "boylam":data[3],
"derinlik":data[4], "ml":data[6]} for data in [liste.split()[0:-1] for liste in kaynak 
if liste.startswith("2020") ][0:5]]

'''width=250, height=150'''
main = Frame(root, pady=1)
main.pack(fill=BOTH)

top = Frame(main, background="blue", pady=5)
top.pack(side=TOP, fill=BOTH)

center = Frame(main)
center.pack(fill=BOTH, pady=0)

lbl = Label(top, background="blue", fg="WHITE", font=("Helvetica", 12), text="Deprem Bilgi Sistemi", pady=5, padx=5)
lbl.pack()

for data in data:
	main = Frame(center, borderwidth=5)
	main.pack(fill=BOTH)
	
	left = Frame(main, borderwidth=0)
	left.pack(fill=BOTH, side=LEFT)

	right = Frame(main, borderwidth=0)
	right.pack(fill=BOTH, side=RIGHT)

	bt1 = Label(left, font="Helvetica 9 bold")
	bt1.config(text="{}".format(" ".join(data.get("bolge"))))
	bt1.grid(row=0, column=0, sticky=W)
	
	bt2 = Label(left)
	bt2.config(text=data.get("tarih"))
	bt2.grid(row=1, column=0, sticky=W)
	
	bt3 = Label(left)
	bt3.config(text= "{}E {}B".format(data.get("enlem"), data.get("boylam")) )
	bt3.grid(row=2, column=0, sticky=W)
	
	bt4 = Label(left)
	bt4.config(text= "{} km".format( data.get("derinlik")) )
	bt4.grid(row=3, column=0, sticky=W)
	
	
	#x= ttk.Separator(main, orient=HORIZONTAL)

	
	bt5 = Label(right, background="red", fg="white", text=data.get("ml"), font="font='Vertica 14 bold")
	bt5.pack()


root.mainloop()  


	

