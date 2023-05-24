class unit:
    HP = 1
    STR = 0
    MAG = 0
    DEX = 0
    SPEED = 0
    LUCK = 0
    DEF = 0
    Items = []
    def __init__(self):
        self.HP = 1
        self.STR = 0
        self.MAG = 0
        self.DEX = 0
        self.SPEED = 0
        self.LUCK = 0
        self.DEF = 0
        self.Items = []
    def pick_class(self):
        print("please choose a class,enter the number next to the class you want")
        print("Guide:")
        print("     HP - your characters hit points")
        print("     STR - used to determine physcal damage")
        print("     MAG - used to determine magical damage and magical resistance")
        print("     DEX - improves hit rate and critacal rate")
        print("     Speed - inflences turn order, avoid rate, and multiple attacks (attack twice if unit's speed > foe's speed + 5 ")
        print("     Luck - can effect many different things")
        print("     DEF - resistance against physcal attacks")
        print("     Skills - any abilits that give each an advantege in battle")
        print("")
        print("")
        print("1 Warrior  HP:52 , str: 12, mag:1 , dex: 4, speed: 6, luck:3 , def:5 , Skills: none, Items: hand axe, shortbow")
        print("2 Sorrcerer  HP:31 , str:5 , mag:9 , dex: 7, speed: 5, luck:4 , def:5 , Skills: none")
        print("3 Monk  HP:28 , str: , mag: , dex: 6, speed: 7, luck: , def:4 , Skills: mircale ( luck % chance to survive a lethal attack)")
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
            self.Items.append("Hand Axe")
            self.Items.append("Short Bow")
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
            self.Items.append("Shortsword")
        elif int(pick) == 5:
            print("your class is a Vagabond")
            self.append = 34
            self.STR = 8;
            self.MAG = 4
            self.DEX = 8
            self.SPEED =11
            self.LUCK = 7
            self.DEF = 6
            self.Items.append("Long Sword")
            self.Items.append("Hand Axe")
        elif int(pick) == 6:
            print("your class is a brigand")
            self.append = 47
            self.STR = 14
            self.MAG = 2
            self.DEX = 2
            self.SPEED =6
            self.LUCK = 6
            self.DEF = 4
            self.Items.append("Battle Axe")
        elif int(pick) == 7:
            print("Your class is a Knight")
            self.append = 43
            self.STR = 13;
            self.MAG = 1
            self.DEX = 7
            self.SPEED =2
            self.LUCK = 3
            self.DEF = 13
            self.Items.append("Long Sword")
            self.Items.append("Lance")
        else:
            print("your class is a deprived")
            self.append = 38
            self.STR = 9
            self.MAG = 9
            self.DEX = 9
            self.SPEED =9
            self.LUCK = 9
            self.DEF = 9
            self.Items.append("rusted knife")
        return
    def printStats(self):
        print("HP: " + str(self.HP))
        print("STR: " + str(self.STR))
        print("MAG: " +str(self.MAG))
        print("DEX: "+str(self.DEX))
        print("SPEED: " +str(self.SPEED))
        print("LUCK: " +str(self.LUCK))
        print("DEF: "+str(self.DEF))
        print("ITEMS:")
        for i in range(0,len(self.Items)):
            print(self.Items[i],end=", ")
        return