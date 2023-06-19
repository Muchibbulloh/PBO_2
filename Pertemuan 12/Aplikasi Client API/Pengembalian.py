import requests
import json
class Pengembalian:
    def __init__(self):
        self.__id=None
        self.__kode = None
        self.__tgl_pengembalian = None
        self.__id_anggota = None
        self.__id_buku = None
        self.__id_petugas = None
        self.__url = "http://localhost/apppengembalian/pengembalian_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode(self):
        return self.__kode
        
    @kode.setter
    def kode(self, value):
        self.__kode = value
    @property
    def tgl_pengembalian(self):
        return self.__tgl_pengembalian
        
    @tgl_pengembalian.setter
    def tgl_pengembalian(self, value):
        self.__tgl_pengembalian = value
    @property
    def id_anggota(self):
        return self.__id_anggota
        
    @id_anggota.setter
    def id_anggota(self, value):
        self.__id_anggota = value
    @property
    def id_buku(self):
        return self.__id_buku
        
    @id_buku.setter
    def id_buku(self, value):
        self.__id_buku = value
    @property
    def id_petugas(self):
        return self.__id_petugas
        
    @id_petugas.setter
    def id_petugas(self, value):
        self.__id_petugas = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kode(self, kode):
        url = self.__url+"?kode="+kode
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_pengembalian']
            self.__kode = item['kode']
            self.__tgl_pengembalian = item['tgl_pengembalian']
            self.__id_anggota = item['id_anggota']
            self.__id_buku = item['id_buku']
            self.__id_petugas = item['id_petugas']
        return data
    def simpan(self):
        payload = {
            "kode":self.__kode,
            "tgl_pengembalian":self.__tgl_pengembalian,
            "id_anggota":self.__id_anggota,
            "id_buku":self.__id_buku,
            "id_petugas":self.__id_petugas
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode(self, kode):
        url = self.__url+"?kode="+kode
        payload = {
            "kode":self.__kode,
            "tgl_pengembalian":self.__tgl_pengembalian,
            "id_anggota":self.__id_anggota,
            "id_buku":self.__id_buku,
            "id_petugas":self.__id_petugas
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kode(self,kode):
        url = self.__url+"?kode="+kode
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text