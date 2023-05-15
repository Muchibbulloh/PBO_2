import pygame
import os

pygame.init()

class Hewan:
    def __init__(self, suara_file):
        self.suara_file = suara_file

    def play_suara(self):
        pygame.mixer.music.load(self.suara_file)
        pygame.mixer.music.play()

class Ayam(Hewan):
    def __init__(self):
        super().__init__('suara\suara-ayam.mp3')
        
class Gajah(Hewan):
    def __init__(self):
        super().__init__('suara/suara-gajah.mp3')
        
class BHantu(Hewan):
    def __init__(self):
        super().__init__('suara/suara-burung-hantu.mp3')
        
class BMerak(Hewan):
    def __init__(self):
        super().__init__('suara/suara-burung-merak.mp3')

class kambing(Hewan):
    def __init__(self):
        super().__init__('suara/suara-kambing.mp3')
        
class Kera(Hewan):
    def __init__(self):
        super().__init__('suara/suara-kera.mp3')
        
class Kuda(Hewan):
    def __init__(self):
        super().__init__('suara/suara-kuda.mp3')

class Kucing(Hewan):
    def __init__(self):
        super().__init__('suara/suara-kucing.mp3')

class Anjing(Hewan):
    def __init__(self):
        super().__init__('suara/suara-anjing.mp3')

class Sapi(Hewan):
    def __init__(self):
        super().__init__('suara/suara-sapi.mp3')

# Membuat list hewan
daftar_hewan = [Ayam(),Gajah(),BHantu(),BMerak(),kambing(),Kera(),Kuda(),Kucing(), Anjing(), Sapi()]

# Memanggil method play_suara() dari setiap hewan dalam list
for hewan in daftar_hewan:
    hewan.play_suara()
    pygame.time.delay(2500)

pygame.quit()