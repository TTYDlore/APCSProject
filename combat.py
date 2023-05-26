from Unit import*;
from Items import*;
class combat:
    p1dmg = 0
    p1hit = 0
    p1avoid = 0
    p1crit = 0
    temp = 0
    order = []
    def entercombat(self,p1,foes):
        while int(p1.HP) >=1:
            print("pick someone to attack")
            for i in range(0,len(foes)):
                print("(" + str(i) + ")" + foes[i].Name + "  " + str(foes[i].HP) + ("/") + str(foes[i].HP))
            print(": ")
            temp = input("")
            print("pick a weapon:")
            return 0
    def sortSpeed(self,p1,foes):
        for e in range(0,len(foes)):
            self.order.append(foes[e])
        self.order.append(p1)
        return