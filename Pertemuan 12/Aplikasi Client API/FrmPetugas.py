import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Petugas import *
class FrmPetugas:
    
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
        Label(mainFrame, text='NAMA:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TELEPON:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ALAMAT:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JK:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKode = Entry(mainFrame) 
        self.txtKode.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtTelepon = Entry(mainFrame) 
        self.txtTelepon.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtAlamat = Entry(mainFrame) 
        self.txtAlamat.grid(row=3, column=1, padx=5, pady=5)
        # Combo Box
        self.txtJk = StringVar()
        Cbo_jk = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJk) 
        Cbo_jk.grid(row=4, column=1, padx=5, pady=5)
        # Adding jk combobox drop down list
        Cbo_jk['values'] = ('L','P')
        Cbo_jk.current()
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_petugas','kode','nama','telepon','alamat','jk')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_petugas', text='ID_PETUGAS')
        self.tree.column('id_petugas', width="50")
        self.tree.heading('kode', text='KODE')
        self.tree.column('kode', width="45")
        self.tree.heading('nama', text='NAMA')
        self.tree.column('nama', width="150")
        self.tree.heading('telepon', text='TELEPON')
        self.tree.column('telepon', width="80")
        self.tree.heading('alamat', text='ALAMAT')
        self.tree.column('alamat', width="80")
        self.tree.heading('jk', text='JK')
        self.tree.column('jk', width="30")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtKode.delete(0,END)
        self.txtKode.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")
        self.txtTelepon.delete(0,END)
        self.txtTelepon.insert(END,"")
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,"")
        self.txtJk.set("")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data petugas
        obj = Petugas()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_petugas"],d["kode"],d["nama"],d["telepon"],d["alamat"],d["jk"]))
    def onCari(self, event=None):
        kode = self.txtKode.get()
        obj = Petugas()
        a = obj.get_by_kode(kode)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode = self.txtKode.get()
        obj = Petugas()
        res = obj.get_by_kode(kode)
        self.txtKode.delete(0,END)
        self.txtKode.insert(END,obj.kode)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,obj.nama)
        self.txtTelepon.delete(0,END)
        self.txtTelepon.insert(END,obj.telepon)
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,obj.alamat)
        self.txtJk.set(obj.jk)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode = self.txtKode.get()
        nama = self.txtNama.get()
        telepon = self.txtTelepon.get()
        alamat = self.txtAlamat.get()
        jk = self.txtJk.get()
        # create new Object
        obj = Petugas()
        obj.kode = kode
        obj.nama = nama
        obj.telepon = telepon
        obj.alamat = alamat
        obj.jk = jk
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
        obj = Petugas()
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
    aplikasi = FrmPetugas(root2, "Aplikasi Data Petugas")
    root2.mainloop()