import pygame as pg

class Display(object):
    WIDTH = 1366
    HEIGHT = 634
    sc=None
    green_chip=None
    red_chip = None
    map=None
    map_rect=None
    font=None
    turn=0

    def __init__(self):
        pg.init()
        self.sc = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption('Monopoly')
        self.green_chip = pg.image.load('greenchip.png')
        self.red_chip = pg.image.load('redchip.png')
        self.green_chip.set_colorkey((0, 0, 0))
        self.red_chip.set_colorkey((0, 0, 0))
        self.green_chip = pg.transform.scale(self.green_chip, (15, 15)).convert()
        self.red_chip = pg.transform.scale(self.red_chip, (15, 15)).convert()
        self.map = pg.image.load('Map.png').convert()
        self.map_rect = self.map.get_rect(center=(self.WIDTH / 2, self.HEIGHT / 2))
        self.font = pg.font.Font(None, 24)
        self.turn=3

    def draw(self,green,red,tiles,msg):
        self.sc.fill((0,0,0))
        self.sc.blit(self.map, self.map_rect)
        green_chip_rect = self.green_chip.get_rect(center=(tiles.mas[green.coor].coors[0] - 2, tiles.mas[green.coor].coors[1]))
        red_chip_rect = self.red_chip.get_rect(center=(tiles.mas[red.coor].coors[0] + 2, tiles.mas[red.coor].coors[1]))
        self.sc.blit(self.green_chip, green_chip_rect)
        self.sc.blit(self.red_chip, red_chip_rect)
        text = self.font.render(msg, True, (255,255,255))
        self.sc.blit(text, (330, 450))

        inv1 = ["Зеленый " + str(green.money) + "тыс $"]
        for i in green.inventory:
            inv1 += [tiles.mas[i].name + " " + str(tiles.mas[i].debt)]
        inv2 = ["Красный " + str(red.money) + "тыс $"]
        for i in red.inventory:
            inv2 += [tiles.mas[i].name + " " + str(tiles.mas[i].debt)]

        i = 0
        for strin in inv1:
            text = self.font.render(strin, True, (255,255,255))
            self.sc.blit(text, (0, i * 30))
            i += 1
        i = 0
        for strin in inv2:
            text = self.font.render(strin, True, (255,255,255))
            self.sc.blit(text, (1200, i * 30))
            i += 1
        pg.display.flip()

    def processing(self,green,red,tiles):
        match self.turn:
            case 0:
                r1, r2 = green.turn()
                if (green.coor + r1 + r2) > 41:
                    green.money += 200
                green.coor = (green.coor + (r1 + r2) * green.next) % 42
                if green.next == 0:
                    msg = "Зеленый пропускает ход"
                else:
                    msg = "Зеленый выбросил " + str(r1) + " и " + str(r2)
            case 1:
                if green.next == -1:
                    green.next = 1
                if green.next != 0:
                    msg = green.main_stage(tiles.mas[green.coor], tiles, red)
                else:
                    msg = "Зеленый пропускает ход"
                    green.next = 1
            case 2:
                r1, r2 = red.turn()
                if (red.coor + r1 + r2) > 41:
                    red.money += 200
                red.coor = (red.coor + (r1 + r2) * red.next) % 42
                if red.next == 0:
                    msg = "Красный пропускает ход"
                else:
                    msg = "Красный выбросил " + str(r1) + " и " + str(r2)
            case 3:
                if red.next == -1:
                    red.next = 1
                if red.next != 0:
                    msg = red.main_stage(tiles.mas[red.coor], tiles, green)
                else:
                    msg = "Красный пропускает ход"
                    red.next = 1
        return False, msg