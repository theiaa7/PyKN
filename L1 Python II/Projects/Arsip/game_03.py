"""
Player and Battle: Implementation and Analyze Result
====================================================
Setelah logic sudah ditambahkan, kita akan menerapkan class menjadi program yang dapat dijalankan.
Caranya, dengan membuat objek atau variabel dari class yang sudah dibuat yang mana nanti akan dimasukan ke method __init__.
Buat object bernama "Mia" sebagai player 1 dan berikan nilai pada setiap attribut.
Example:
    mia.name = "Mia"
    mia.lp = 100
    mia.deff = 20
    mia.atk =  120

mia.name artinya kita memberikan nama untuk object player. Attribute ini kita gunakan untuk mencetak namanya saat di jalankan.
Lakukan hal serupa untuk player 2 dengan nama, for example "Johnson".
Setelah selesai, buat object/variabel game dari class Battle. Buat perulangan object game untuk menjalankan gamenya secara terus menerus
sampai game mendapatkanm pemenang.
"""

import random
import time


class Player:

    def __init__(self):
        self.name = ''
        self.lp = 0
        self.atk = 0
        self.deff = 0

    def attacked(self, another_player):
        self.lp = self.lp - (another_player.atk - self.deff)


class Battle:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.random_turn = 0

    def run(self):
        self.random_turn = random.randint(10, 100)
        print_turn = True
        is_running = True
        print(f'{self.player1.name} LP: {self.player1.lp} | {self.player2.name} LP: {self.player2.lp},')
        if self.random_turn % 2 == 0:
            print_turn = False
            self.player2.attacked(self.player1)
        else:
            self.player1.attacked(self.player2)

        if self.player1.lp <= 0:
            is_running = False
            message = {
                "is_running": is_running,
                "msg": "player 2 win"
            }
            return message

        elif self.player2.lp <= 0:
            is_running = False
            message = {
                "is_running": is_running,
                "msg": "player 1 win"
            }
            return message
        else:
            message = {
                "is_running": is_running,
                "msg": f"calculating {'Player 1 attack' if print_turn else 'Player 2 attack'}"
            }
            return message


# add implementation and analyze the results
mia = Player()
mia.name = "Mia"
mia.lp = 600
mia.deff = 20
mia.atk = 120

johnson = Player()
johnson.name = "John"
johnson.lp = 600
johnson.deff = 20
johnson.atk = 120

game = Battle(mia, johnson)

while True:
    arena_battle = game.run()
    print(arena_battle["msg"])
    if not arena_battle["is_running"]:
        break

    time.sleep(1)


