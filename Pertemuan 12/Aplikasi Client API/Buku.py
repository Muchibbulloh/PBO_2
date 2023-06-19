import requests
import json
class Buku:
    def __init__(self):
        self.__id=None
        self.__kode = None
        self.__judul = None
        self.__penulis = None
        self.__url = "http://localhost/appbuku/buku_api.php"
                    
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
    def judul(self):
        return self.__judul
        
    @judul.setter
    def judul(self, value):
        self.__judul = value
    @property
    def penulis(self):
        return self.__penulis
        
    @penulis.setter
    def penulis(self, value):
        self.__penulis = value
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
            self.__id = item['id_buku']
            self.__kode = item['kode']
            self.__judul = item['judul']
            self.__penulis = item['penulis']
        return data
    def simpan(self):
        payload = {
            "kode":self.__kode,
            "judul":self.__judul,
            "penulis":self.__penulis
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode(self, kode):
        url = self.__url+"?kode="+kode
        payload = {
            "kode":self.__kode,
            "judul":self.__judul,
            "penulis":self.__penulis
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