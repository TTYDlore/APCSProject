import random
from Items import*;
class unit:
    HP = 1
    STR = 0
    MAG = 0
    DEX = 0
    SPEED = 0
    LUCK = 0
    DEF = 0
    items = []
    Mana = 0
    Rank = 0
    rustedknife = Items("Rusted Knife", 3,70,10,0,0)
    knife = Items("Knife",5,85,15,0,0)
    shortsword = Items("Short Sword",7,90,0,0,0)
    longsword = Items("Long Sword",11,80,0,0,0)
    Claymore = Items("Claymore",14,70,0,0,0)
    broadsword = Items("Broadsword",17,60,0,0,0)
    scimitar = Items("Scimitar",10,70,35,0,0)
    estoc = Items("Estoc",9,75,10,0,0)
    Moonlight = Items("Moonlight Greatsword",21,80,10,1,0)
    pike = Items("Pike",8,85,0,0,0)
    lance = Items("Lance",12,75,0,0,0)
    javalin = Items("Javalin",17,60,0,0,0)
    spear = Items("Spear",19,70,5,0,0)
    handaxe = Items("Hand Axe",9,80,0,0,0)
    battleaxe = Items("Battle Axe",13,70,0,0,0)
    tomahawk = Items("Tomahawk",15,75,10,0,0)
    shortbow = Items("Short Bow", 6,90,5,0,0)
    longbow = Items("Longbow",10,80,5,0,0)
    killerbow = Items("Killer Bow",9,70,40,0,0)
    fire = Items("Fire",7,90,0,1,1)
    thunder = Items("Thunder",8,80,15,1,2)
    heal = Items("Heal",0,100,0,3,3)
    def __init__(self):
        self.HP = 1
        self.STR = 0
        self.MAG = 0
        self.DEX = 0
        self.SPEED = 0
        self.LUCK = 0
        self.DEF = 0
    def getRank(self):
        self.Rank = (int(self.HP)/2) + (int(self.STR)) + (int(self.MAG)) + (int(self.DEX)) + (int(self.SPEED)) + (int(self.LUCK)) + (int(self.DEF))
    def setName(self,a):
        self.Name = str(a)
    def pick_class(self):
        print("please choose a class,enter the number next to the class you want")
        print("Guide:")
        print("     HP - your characters hit points")
        print("     STR - used to determine physcal damage")
        print("     MAG - used to determine magical damage and magical resistance")
        print("     DEX - improves hit rate and critacal rate")
        print("     Speed - inflences turn order, avoid rate, and multiple attacks (attack twice if unit's speed > foe's speed + 5 and vice versa")
        print("     Luck - can effect many different things")
        print("     DEF - resistance against physcal attacks")
        print("     Skills - any abilits that give each an advantege in battle")
        print("")
        print("")
        print("1 Warrior  HP:52 , str: 12, mag:1 , dex: 4, speed: 6, luck:3 , def:5 , Skills: none, Items: hand axe, shortbow")
        print("2 Sorrcerer  HP:31 , str:5 , mag:11 , dex: 7, speed: 5, luck:4 , def:5 , Skills: none")
        print("3 Monk  HP:28 , str:7 , mag:9 , dex: 6, speed: 7, luck: , def:4 , Skills: mircale ( luck % chance to survive a lethal attack)")
        print("4 Theif  HP:29 , str:6 , mag:5 , dex: 11, speed: 8, luck:10 , def:4 , Skills: none, Items: Shortsword")
        print("5 Vagabond  HP:35 , str:8 , mag:4 , dex: 8, speed: 11, luck:7 , def:6 , Skills: pursuit (changes muliti attack formula (if unit's speed > foes speed)), Items: Long sword, handaxe")
        print("6 Brigand  HP: 47 , str: 14, mag: 2, dex: 2, speed: 6, luck: 6, def: 4, Skills: none, Items: Battle AXe")
        print("7 Knight  HP: 43, Str: 13, Mag: 1, dex: 7, Speed:2, luck: 3, def: 13, Skiils: Big Sheild(luck % chance to negate pyshical damage), Items: Long Sword, Lance")
        print("10 Deprived  HP: 38, str:9 , mag: 9, dex: 9, speed: 9, luck: 9, def: 9, Skills: none, Items: rusted knife")
        pick = input("")
        if int(pick) == 1:
            print("your class is a Warrior")
            self.append = 52
            self.STR = 12;
            self.MAG = 1
            self.DEX = 4
            self.SPEED =6
            self.LUCK = 3
            self.DEF = 5
            self.Mana = self.MAG
            self.items.append(self.handaxe)
            self.items.append(self.shortbow)
        elif int(pick) == 2:
            print("your class is a Sorrcerer")
        elif int(pick) == 3:
            print("Your class is a Monk")
        elif int(pick) == 4:
            print("Your class is a theif")
            self.append = 29
            self.STR = 6;
            self.MAG = 5
            self.DEX = 11
            self.SPEED =8
            self.LUCK = 10
            self.DEF = 4
            self.Mana = self.MAG
            self.items.append(self.shortsword)
        elif int(pick) == 5:
            print("your class is a Vagabond")
            self.append = 34
            self.STR = 8;
            self.MAG = 4
            self.DEX = 8
            self.SPEED =11
            self.LUCK = 7
            self.DEF = 6
            self.Mana = self.MAG
            self.items.append(self.longsword)
            self.items.append(self.handaxe)
        elif int(pick) == 6:
            print("your class is a brigand")
            self.append = 47
            self.STR = 14
            self.MAG = 2
            self.DEX = 2
            self.SPEED =6
            self.LUCK = 6
            self.DEF = 4
            self.Mana = self.MAG
            self.items.append(self.battleaxe)
        elif int(pick) == 7:
            print("Your class is a Knight")
            self.append = 43
            self.STR = 13;
            self.MAG = 1
            self.DEX = 7
            self.SPEED =2
            self.LUCK = 3
            self.DEF = 13
            self.Mana = self.MAG
            self.items.append(self.longsword)
            self.items.append(self.lance)
        else:
            print("your class is a deprived")
            self.append = 38
            self.STR = 9
            self.MAG = 9
            self.DEX = 9
            self.SPEED =9
            self.LUCK = 9
            self.DEF = 9
            self.Mana = self.MAG
            self.items.append(self.rustedknife)
        return
    def printStats(self):
        print("HP: " + str(self.HP))
        print("STR: " + str(self.STR))
        print("MAG: " +str(self.MAG))
        print("DEX: "+str(self.DEX))
        print("SPEED: " +str(self.SPEED))
        print("LUCK: " +str(self.LUCK))
        print("DEF: "+str(self.DEF))
        print("MANA: " + str(self.Mana))
        print("ITEMS:")
        for i in range(0,len(self.items)):
            self.items[i].printName()
        return
    def genericVillager1(self):
        self.HP = int(random.randrange(8,20))
        self.STR = int(random.randrange(0,6))
        self.MAG = int(random.randrange(0,3))
        self.DEX = int(random.randrange(0,5))
        self.SPEED = int(random.randrange(0,4))
        self.LUCK = int(random.randrange(0,2))
        self.DEF = int(random.randrange(0,3))
        self.Mana = self.MAG
        temp = random.randrange(1,101)
        if int(temp) >= 95:
            self.items.append(self.longsword)
        elif int(temp) >= 63:
            self.items.append(self.shortsword)
        else: 
            self.items.append(self.rustedknife)
    def gennericVillager2(self):
        self.HP = int(random.randrange(4,16))
        self.STR = int(random.randrange(0,5))
        self.MAG = int(random.randrange(0,2))
        self.DEX = int(random.randrange(0,7))
        self.SPEED = int(random.randrange(0,6))
        self.LUCK = int(random.randrange(0,2))
        self.DEF = int(random.randrange(0,2))
        self.Mana = self.MAG
        temp = random.randrange(1,101)
        if int(temp) >= 95:
            self.items.append(self.killerbow)
        elif int(temp) >= 56:
            self.items.append(self.longbow)
        else: 
            self.items.append(self.shortbow)
    def gennericVillager3(self):
        self.HP = int(random.randrange(10,23))
        self.STR = int(random.randrange(2,6))
        self.MAG = int(random.randrange(4,6))
        self.DEX = int(random.randrange(0,3))
        self.SPEED = int(random.randrange(2,3))
        self.LUCK = int(random.randrange(0,1))
        self.DEF = int(random.randrange(3,6))
        self.Mana = self.MAG
        temp = random.randrange(1,101)
        if int(temp) >= 81:
            self.items.append(self.longsword)
            self.items.append(self.thunder)
        elif int(temp) >= 41:
            self.items.append(self.shortsword)
            self.items.append(self.fire)
        else: 
            self.items.append(self.fire)
    def villBoss1(self):   #halberdier boss
        self.HP = int(random.randrange(30,35))
        self.STR = int(random.randrange(7,10))
        self.MAG = int(random.randrange(3,5))
        self.DEX = int(random.randrange(8,12))
        self.SPEED = int(random.randrange(6,9))
        self.LUCK = int(random.randrange(2,5))
        self.DEF = int(random.randrange(4,7))
        self.Mana = self.MAG
        temp = random.randrange(1,101)
        if int(temp) >= 51:
            self.items.append(self.lance)
            self.items.append(self.shortsword)
        else: 
            self.items.append(self.pike)
            self.items.append(self.longsword)
    def villBoss2(self): # General Boss
        self.HP = int(random.randrange(32,34))
        self.STR = int(random.randrange(8,12))
        self.MAG = int(random.randrange(0,2))
        self.DEX = int(random.randrange(9,13))
        self.SPEED = int(random.randrange(1,5))
        self.LUCK = int(random.randrange(2,5))
        self.DEF = int(random.randrange(7,14))
        self.Mana = self.MAG
        temp = random.randrange(1,101)
        if int(temp) >= 66:
            self.items.append(self.javalin)
            self.items.append(self.longbow)
        elif int(temp) >= 33:
            self.items.append(self.handaxe)
            self.items.append(self.Claymore)
        else: 
            self.items.append(self.battleaxe)
            self.items.append(self.shortbow)