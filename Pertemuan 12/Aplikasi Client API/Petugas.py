import requests
import json
class Petugas:
    def __init__(self):
        self.__id=None
        self.__kode = None
        self.__nama = None
        self.__telepon = None
        self.__alamat = None
        self.__jk = None
        self.__url = "http://localhost/apppetugas/petugas_api.php"
                    
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
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, value):
        self.__nama = value
    @property
    def telepon(self):
        return self.__telepon
        
    @telepon.setter
    def telepon(self, value):
        self.__telepon = value
    @property
    def alamat(self):
        return self.__alamat
        
    @alamat.setter
    def alamat(self, value):
        self.__alamat = value
    @property
    def jk(self):
        return self.__jk
        
    @jk.setter
    def jk(self, value):
        self.__jk = value
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
            self.__id = item['id_petugas']
            self.__kode = item['kode']
            self.__nama = item['nama']
            self.__telepon = item['telepon']
            self.__alamat = item['alamat']
            self.__jk = item['jk']
        return data
    def simpan(self):
        payload = {
            "kode":self.__kode,
            "nama":self.__nama,
            "telepon":self.__telepon,
            "alamat":self.__alamat,
            "jk":self.__jk
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode(self, kode):
        url = self.__url+"?kode="+kode
        payload = {
            "kode":self.__kode,
            "nama":self.__nama,
            "telepon":self.__telepon,
            "alamat":self.__alamat,
            "jk":self.__jk
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