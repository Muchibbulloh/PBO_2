import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Peminjaman import *
class FrmPeminjaman:
    
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
        Label(mainFrame, text='TANGGAL_PINJAM:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TANGGAAL_KEMBALI:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ID_BUKU:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ID_ANGGOTA:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ID_PETUGAS:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKode = Entry(mainFrame) 
        self.txtKode.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtTanggal_pinjam = Entry(mainFrame) 
        self.txtTanggal_pinjam.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtTanggaal_kembali = Entry(mainFrame) 
        self.txtTanggaal_kembali.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtId_buku = Entry(mainFrame) 
        self.txtId_buku.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtId_anggota = Entry(mainFrame) 
        self.txtId_anggota.grid(row=4, column=1, padx=5, pady=5)
        # Textbox
        self.txtId_petugas = Entry(mainFrame) 
        self.txtId_petugas.grid(row=5, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_peminjaman','kode','tanggal_pinjam','tanggaal_kembali','id_buku','id_anggota','id_petugas')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_peminjaman', text='ID_PEMINJAMAN')
        self.tree.column('id_peminjaman', width="30")
        self.tree.heading('kode', text='KODE')
        self.tree.column('kode', width="45")
        self.tree.heading('tanggal_pinjam', text='TANGGAL_PINJAM')
        self.tree.column('tanggal_pinjam', width="100")
        self.tree.heading('tanggaal_kembali', text='TANGGAAL_KEMBALI')
        self.tree.column('tanggaal_kembali', width="100")
        self.tree.heading('id_buku', text='ID_BUKU')
        self.tree.column('id_buku', width="55")
        self.tree.heading('id_anggota', text='ID_ANGGOTA')
        self.tree.column('id_anggota', width="40")
        self.tree.heading('id_petugas', text='ID_PETUGAS')
        self.tree.column('id_petugas', width="40")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtKode.delete(0,END)
        self.txtKode.insert(END,"")
        self.txtTanggal_pinjam.delete(0,END)
        self.txtTanggal_pinjam.insert(END,"")
        self.txtTanggaal_kembali.delete(0,END)
        self.txtTanggaal_kembali.insert(END,"")
        self.txtId_buku.delete(0,END)
        self.txtId_buku.insert(END,"")
        self.txtId_anggota.delete(0,END)
        self.txtId_anggota.insert(END,"")
        self.txtId_petugas.delete(0,END)
        self.txtId_petugas.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data peminjaman
        obj = Peminjaman()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_peminjaman"],d["kode"],d["tanggal_pinjam"],d["tanggaal_kembali"],d["id_buku"],d["id_anggota"],d["id_petugas"]))
    def onCari(self, event=None):
        kode = self.txtKode.get()
        obj = Peminjaman()
        a = obj.get_by_kode(kode)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode = self.txtKode.get()
        obj = Peminjaman()
        res = obj.get_by_kode(kode)
        self.txtKode.delete(0,END)
        self.txtKode.insert(END,obj.kode)
        self.txtTanggal_pinjam.delete(0,END)
        self.txtTanggal_pinjam.insert(END,obj.tanggal_pinjam)
        self.txtTanggaal_kembali.delete(0,END)
        self.txtTanggaal_kembali.insert(END,obj.tanggaal_kembali)
        self.txtId_buku.delete(0,END)
        self.txtId_buku.insert(END,obj.id_buku)
        self.txtId_anggota.delete(0,END)
        self.txtId_anggota.insert(END,obj.id_anggota)
        self.txtId_petugas.delete(0,END)
        self.txtId_petugas.insert(END,obj.id_petugas)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode = self.txtKode.get()
        tanggal_pinjam = self.txtTanggal_pinjam.get()
        tanggaal_kembali = self.txtTanggaal_kembali.get()
        id_buku = self.txtId_buku.get()
        id_anggota = self.txtId_anggota.get()
        id_petugas = self.txtId_petugas.get()
        # create new Object
        obj = Peminjaman()
        obj.kode = kode
        obj.tanggal_pinjam = tanggal_pinjam
        obj.tanggaal_kembali = tanggaal_kembali
        obj.id_buku = id_buku
        obj.id_anggota = id_anggota
        obj.id_petugas = id_petugas
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
        obj = Peminjaman()
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
    aplikasi = FrmPeminjaman(root2, "Aplikasi Data Peminjaman")
    root2.mainloop()