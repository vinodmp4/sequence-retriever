import web
from tkinter import *
import threading

class GUI:
    def __init__(self,parent):
        self.parent=parent
        self.parent.geometry('850x600')
        self.parent.configure(background="#FFFFFF")
        self.parent.title("Sequence Retriever")
        self.sequence=""
        self.mainframe = Frame(self.parent)
        self.mainframe.pack(fill=BOTH)
        self.setimportpage()
        self.updateconsole('Ready')       

    def setimportpage(self):
        self.importframe0 = Frame(self.mainframe)
        self.scrollbar0=Scrollbar(self.importframe0)
        self.console = Text(self.importframe0,height=10,yscrollcommand=self.scrollbar0.set)
        self.console.config(state="disabled",background="#000000",foreground="#00FF00")
        self.scrollbar0.config(command=self.console.yview)
        self.scrollbar0.pack(side=RIGHT,fill=Y)
        self.console.pack(side=BOTTOM,fill=X,expand=1)
        self.importframe0.pack(side=BOTTOM,fill=X,expand=1)
        self.importframe2 = Frame(self.mainframe)
        self.serverlist = ['NCBI','PDB','UNIPROT']
        self.accessiontext = StringVar()
        self.dropdowntext = StringVar()
        self.dropdowntext.set('NCBI')
        self.infolabel1 = Label(self.importframe2,text="Enter Accession Number: ")
        self.servername = OptionMenu(self.importframe2,self.dropdowntext,*self.serverlist)
        self.servername.config(width=10)
        self.accessionentry = Entry(self.importframe2,width=300,textvariable=self.accessiontext)
        self.retrievebutton = Button(self.importframe2,text="Retreive",background="#004400",foreground="#FFFFFF",command=self.retrievesequence)
        self.clearbutton2 = Button(self.importframe2,text="Clear",background="#440000",foreground="#FFFFFF",command=self.clearaccession)
        self.infolabel1.pack(side=LEFT)
        self.servername.pack(side=LEFT)
        self.clearbutton2.pack(side=RIGHT)
        self.retrievebutton.pack(side=RIGHT)
        self.accessionentry.pack(side=LEFT,expand=1,fill=X)
        self.importframe2.pack(side=TOP,fill=X)
        self.importframe4 = Frame(self.mainframe,height=30)
        self.scrollbar1=Scrollbar(self.importframe4)
        self.sequencebox = Text(self.importframe4,width=30,height=300,yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.sequencebox.yview)
        self.scrollbar1.pack(side=RIGHT,fill=Y)
        self.sequencebox.pack(side=LEFT,fill=BOTH,expand=1)
        self.importframe4.pack(side=TOP,fill=X,expand=1)

    def updateconsole(self,command):
        self.console.config(state="normal")
        self.console.insert("end",("\n"+command))
        self.console.see("end")
        self.console.config(state="disabled")

    def updatesequencebox(self,text):
        self.sequencebox.delete('1.0','end')
        self.sequencebox.insert('end',text)

    def dothreading(self):
        self.runapssp2button.config(state='disabled')
        predictedobject = web.predictstructure(self,self.sequence)
        self.runapssp2button.config(state='normal')

    def _threadingprediction(self):
        t= threading.Thread(target=self.dothreading)
        t.daemon=True
        t.start()
            
    def doretrievefastathread(self):
        self.retrievebutton.config(state='disabled')
        fastaobj = web.fasta(self,self.accessionentry.get(),self.serverlist.index(self.dropdowntext.get()))
        self.sequence = fastaobj.sequence
        self.updatesequencebox(fastaobj.result)
        self.retrievebutton.config(state='normal')
        
    def retrievesequence(self):
        if len(self.accessionentry.get())<= 0:
            self.updateconsole("Error: Enter an Accession Id")
        else:
            self.updateconsole("Accession Id: "+self.accessionentry.get()+" || Connecting to "+self.dropdowntext.get()+" server...")
            f= threading.Thread(target=self.doretrievefastathread)
            f.daemon=True
            f.start()

    def clearaccession(self):
        self.accessionentry.delete(0,'end')
                

if __name__ == "__main__":
    application = Tk()
    window = GUI(application)
    application.mainloop()
