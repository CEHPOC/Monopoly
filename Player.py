import random


class Player(object):
    money=0
    inventory=[]
    coor=0
    number=0
    next=1
    def __init__(self,number):
        self.money=2000
        self.inventory=[]
        self.coor=0
        self.number=number
        self.next=1

    def turn(self):
        r1=random.randint(1,6)
        r2 = random.randint(1, 6)
        return [r1,r2]

    def buy(self,tile,mas):
        if self.money > tile.price:
            self.money-=tile.price
            tile.owner = self.number
            self.inventory.append(mas.index(tile))
            return True
        else:
            return False

    def pay(self,tile,other):
        other.money +=tile.debt
        if self.money > tile.debt:
            self.money -= tile.debt
            return True
        else:
            return False

    def pawn(self,tile,mas):
        if tile in self.inventory:
            self.inventory.remove(tile)
            self.money+=0.75*mas[tile].price
            mas[tile].debt=0
            print(mas[tile].name)

    def main_stage(self, tile, mas,other):
        msg=""
        if tile.owner==self.number:
            msg="Игрок попал на свою клетку"
            pass
        elif tile.owner == 3-self.number:
            while not self.pay(tile,other):
                self.pawn(self.inventory[random.randint(0, len(self.inventory) - 1)],mas.mas)
            msg = "Игрок заплатил пошлину "+str(tile.debt)+"тыс $"
        elif tile.owner == 0:
            if not self.buy(tile, mas.mas):
                if random.random() <= 0.3:
                    while self.buy(tile,mas.mas):
                        self.pawn(self.inventory[random.randint(0, len(self.inventory) - 1)])
                    msg="Игрок купил поле " + tile.name
                else:
                    msg="Игрок решил не покупать поле " + tile.name
            else:
                msg="Игрок купил поле "+tile.name
        else:
            match tile.name:
                case 'Старт':
                    self.money += 200
                    msg="Игрок попал на старт и получил дополнительно 200 тыс &"
                case 'Налог':
                    msg="Игрок заплатил налог "+str(int(self.money * 0.2))+" тыс $"
                    self.money = int(self.money * 0.8)
                case 'Лотерея':
                    if random.random() <= 0.5:
                        self.money += 100
                        msg = "Игрок выиграл в лотерее 100 тыс &"
                    else:
                        self.money -= 100
                        msg = "Игрок проиграл в лотерее 100 тыс &"
                case 'Таможня':
                    self.coor = 34
                    msg = "Игрок отправляется в отпуск"
                case 'Отпуск':
                    self.coor = 13
                    msg = "Игрок отправляется на таможню"
                case 'Назад':
                    self.next = -1
                    msg = "Игрок в следущий ход пойдет в другую сторону"
                case 'Пропуск':
                    self.next = 0
                    msg = "Игрок пропускает следующий ход"
                case 'Джекпот':
                    self.money+=350
                    msg = "Игрок выиграл 350 тыс $"
        return msg





