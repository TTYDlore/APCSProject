import random
from Unit import*;
from combat import*;
p1 = unit()
foes = []
print(p1.STR)
test = combat()
p1.pick_class()
p1dmg = int(0)
p1hit = int(0)
f1 = unit()
f1max = 0
f2 = unit()
f2max = 0
f3= unit()
f3max = 0
b = unit()
gameover = int(0)
print("see how long you can last")
print("")
print("")
print("As you wake up you can see the great corupted town of Grado, once a peacful town until the townsfolk")
print("started attaking each other. Even the guards are effected by this maddnes. You have been sent to the ")
print("village to 'take care' of the problem, when you arrive you have three options ahead of you.")
print("enter the number of where you would like to go frist:")
print("(1) the town center")
print("(2) a nearby inn")
print("(3) the town's barracks")
pick = input("")
if int(pick) == 1:
    while gameover == 0:
        print("you walk toward the town square and you see a lone corupted villager")
        f1.genericVillager1()
        f1.setName("corupted vill.")
        f1max = int(f1.HP)
        foes.append(f1)
        test.sortSpeed(p1,foes)
        test.entercombat(p1,foes)
elif int(pick) == 2:
    while gameover == 0:
        print("you walk")
else:
    while gameover == 0:
        print("you enter the barracks ")
