"""
Player and Battle: Add Game Logic
=================================
Di dalam class Player, kita akan menambahkan logic rumus untuk mengurangi nilai life point.

Rumusnya:
    player1.lp = player1.lp - (another_player.atk - player1.deff)
    lp adalah life point
    atk adalah nilai attack
    deff adalah nilai defend

Di dalam class Battle, kita akan menambahkan logic untuk menerapkan rumus di atas pada tiap putaran (turn).
Jika lp player masih lebih dari 0, maka akan dilakukan battle sekali lagi hingga nilainya dibawah atau sama dengan 0.
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
        # (1) implemented logic for attacked calculation
        self.lp = self.lp - (another_player.atk - self.deff)


class Battle:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.random_turn = 0

    def run(self):
        # (2) after create attacked method logic, implemented logic for battling
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
            x = ""
            if print_turn:
                x = "Player 1 attack"
            else:
                x = "Player 2 attach"
            message = {
                "is_running": is_running,
                "msg": f"calculating {x}"
            }
            return message


