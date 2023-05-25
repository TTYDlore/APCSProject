class Items:
    name = ""
    might = ""
    hit = ""
    crit =""
    TYPE =""
    cost = ""
    def __init__ (self,a,b,c,d,e,f):
        self.name = str(a)
        self.might = b
        self.hit = c
        self.crit = d
        self.TYPE = e
        self.cost = f
    def printName(self):
        print(self.name + ", Damage: " + str(self.might) + ", Hit: " + str(self.hit) + ", Crit: " + str(self.crit))
        return
    