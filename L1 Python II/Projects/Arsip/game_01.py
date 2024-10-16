
import random
import time

"""
Game Showcase
=============
Beri tahu siswa di sini kita akan membuat game sederhana dengan Class dan Method.
Show project akhir ke student dan jalankan beberapa kali.

Basic Class
===========
The teacher teach student about class and method.
Class adalah prototype, atau blueprint, atau rancangan yang mendefinisikan variable dan method-methode pada seluruh objek tertentu.
Class berfungsi untuk menampung isi dari program yang akan di jalankan, di dalamnya berisi atribut / type data dan method untuk menjalankan suatu program.

Method
======
Method adalah kumpulan program yang mempunyai nama. Method merupakan sarana bagi programmer untuk memecah program menjadi bagian-bagian yang kecil agar jadi lebih kompleks sehingga dapat di gunakan berulang-ulang.
Method merupakan suatu operasi berupa fungsi-fungsi yang dapat dikerjakan oleh suatu object. Method didefinisikan pada class akan tetapi dipanggil melalui object.
Method adalah aksi dari sebuah class. Contohnya, class Manusia bisa beraksi seeprti jalan, makan, minum etc.

Player and Battle: Create Class and Method
==========================================
Buat sebuah class dengan nama Player and Battle.
Di dalam class Player dan Battle ada method __init__.
    Fungsi method __init__ untuk menginisialisasi attribut pada sebuah class.
    Attribute adalah variabel milik kelas. Contohnya, class Manusia memiliki atribut name, age, warna kulit etc.
Selanjutnya, pada classclass Player buatlah method dengan nama attacked. Method attack berisi rumus untuk mengurangi life point player.
 saat ini, agar program bisa dijalankan, kita 
harus memberikan statement pass.
Terakhir, pada class Battle, buatlah sebuah method dengan nama run. Method run ini berfungsi untuk menghitung
attribute life point dari masing-masing player jika diserang pada tiap putaran (turn).
"""

class Player:
    def __init__(self):
        self.name = ''
        self.lp = 0
        self.atk = 0
        self.deff = 0

    def attacked(self, another_player):
        pass


class Battle:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.random_turn = 0

    def run(self):
        pass



