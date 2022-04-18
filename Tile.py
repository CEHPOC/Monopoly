


class Tile(object):
    owner=0
    name=''
    price=0
    debt=0
    coors=(0,0)
    def __init__(self,owner,name,price,debt,coors):
        self.owner=owner
        self.name = name
        self.price = price
        self.debt = debt
        self.coors = coors