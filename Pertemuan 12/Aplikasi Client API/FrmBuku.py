import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Buku import *
class FrmBuku:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='KODE:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JUDUL:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PENULIS:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKode = Entry(mainFrame) 
        self.txtKode.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtJudul = Entry(mainFrame) 
        self.txtJudul.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtPenulis = Entry(mainFrame) 
        self.txtPenulis.grid(row=2, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_buku','kode','judul','penulis')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_buku', text='ID_BUKU')
        self.tree.column('id_buku', width="50")
        self.tree.heading('kode', text='KODE')
        self.tree.column('kode', width="50")
        self.tree.heading('judul', text='JUDUL')
        self.tree.column('judul', width="180")
        self.tree.heading('penulis', text='PENULIS')
        self.tree.column('penulis', width="150")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtKode.delete(0,END)
        self.txtKode.insert(END,"")
        self.txtJudul.delete(0,END)
        self.txtJudul.insert(END,"")
        self.txtPenulis.delete(0,END)
        self.txtPenulis.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data buku
        obj = Buku()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_buku"],d["kode"],d["judul"],d["penulis"]))
    def onCari(self, event=None):
        kode = self.txtKode.get()
        obj = Buku()
        a = obj.get_by_kode(kode)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode = self.txtKode.get()
        obj = Buku()
        res = obj.get_by_kode(kode)
        self.txtKode.delete(0,END)
        self.txtKode.insert(END,obj.kode)
        self.txtJudul.delete(0,END)
        self.txtJudul.insert(END,obj.judul)
        self.txtPenulis.delete(0,END)
        self.txtPenulis.insert(END,obj.penulis)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode = self.txtKode.get()
        judul = self.txtJudul.get()
        penulis = self.txtPenulis.get()
        # create new Object
        obj = Buku()
        obj.kode = kode
        obj.judul = judul
        obj.penulis = penulis
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kode(kode)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kode = self.txtKode.get()
        obj = Buku()
        obj.kode = kode
        if(self.ditemukan==True):
            res = obj.delete_by_kode(kode)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmBuku(root2, "Aplikasi Data Buku")
    root2.mainloop()
