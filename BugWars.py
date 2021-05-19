import random

class Bug():
    def __init__(self, ID, role, attack, health, defense, sub, orders):
        self.ID = ID,
        self.role = role,
        self.attack = attack,
        self.health = health,
        self.defense = defense
        self.sub = sub
        self.orders = orders

    def damaged(self, dam):
        #the first time converts the health (tuple) into int
        try:
            for i in self.health: #throws error if self.health is already an int
                h = i
            h -= dam
            self.health = h
            print("{} has {} health remaining".format(self.ID, self.health))
        #if health is already an int it will throw an error above, this except then minuses a int with int
        except:
            self.health -= dam
        if self.health <= 0:
            self.orders = "dead"


    def order(self, message):
        for i in self.sub:
            i.orders = message
            i.acknowledge()

    def communicate(self, reciever, message):
        pass

    def acknowledge(self):
        print(self.ID, " orders are now ", self.orders)

A1001 = Bug("A1001", "Soldier", 3, 5, 1, [], "none")
A1002 = Bug("A1002", "Soldier", 3, 5, 1, [], "none")
A1003 = Bug("A1003", "Soldier", 3, 5, 1, [], "none")
A1004 = Bug("A1004", "Soldier", 3, 5, 1, [], "none")
A2001 = Bug("A2001", "Beta", 5, 10, 2, [A1001, A1002, A1003, A1004], "none")

A1005 = Bug("A1005", "Soldier", 3, 5, 1, [], "none")
A1006 = Bug("A1006", "Soldier", 3, 5, 1, [], "none")
A1007 = Bug("A1007", "Soldier", 3, 5, 1, [], "none")
A1008 = Bug("A1008", "Soldier", 3, 5, 1, [], "none")
A2002 = Bug("A2002", "Beta", 5, 10, 2, [A1001, A1002, A1003, A1004], "none")

Ycaptains = [A2001, A2002]


B1001 = Bug("B1001", "Soldier", 3, 5, 1, [], "none")
B1002 = Bug("B1002", "Soldier", 3, 5, 1, [], "none")
B1003 = Bug("B1003", "Soldier", 3, 5, 1, [], "none")
B1004 = Bug("B1004", "Soldier", 3, 5, 1, [], "none")
B2001 = Bug("B2001", "Beta", 5, 10, 2, [B1001, B1002, B1003, B1004], "none")

B1005 = Bug("B1005", "Soldier", 3, 5, 1, [], "none")
B1006 = Bug("B1006", "Soldier", 3, 5, 1, [], "none")
B1007 = Bug("B1007", "Soldier", 3, 5, 1, [], "none")
B1008 = Bug("B1008", "Soldier", 3, 5, 1, [], "none")
B2002 = Bug("B2002", "Beta", 5, 10, 2, [B1005, B1006, B1007, B1008], "none")

Ecaptains = [B2001, B2002]

def battle(fighters, defenders):
    #takes each fighter and has it attack against 1 random defender
    for a in fighters.sub:
        leader = random.randint(0, len(defenders.sub))
        if len(defenders.sub) >= 1: #checks to see if the leader has any subs left
            d = defenders.sub[random.randint(0, len(defenders.sub)-1)]
        else:
            d = defenders
        for i in a.attack:
            n = i
        hit = random.randint(0, n)
        #print(a.ID, "attacks with a ", hit, " against ", d.defense)
        if leader == len(defenders.sub): #fighter attacks the leader
            if hit > defenders.defense:
                hit -= defenders.defense
                print("{} attacks {} for {} damage!".format(a.ID, defenders.ID, hit))
                d.damaged(hit)
            else:
                print("{} attacks {} but misses!".format(a.ID, defenders.ID))

        elif hit > d.defense:
            hit -= d.defense
            print("{} attacks {} for {} damage!".format(a.ID, d.ID, hit))
            d.damaged(hit)
        else:
            print("{} attacks {} but misses!".format(a.ID, d.ID))

        if d.health == 0:  
            for i, o in enumerate(defenders.sub): #checks the defenders soldiers to find the dead one
                if o.orders == "dead":
                    del defenders.sub[i]
                    print(o.ID, "died")
                    break
    leader = random.randint(0, len(defenders.sub))
    #checks to see if the leader has any subs left
    if len(defenders.sub) >= 1:
        d = defenders.sub[random.randint(0, len(defenders.sub)-1)]
    else:
        d = defenders
    for i in fighters.attack:
        n = i
    hit = random.randint(0, n)
    if leader == len(defenders.sub): #fighter attacks the leader
        if hit > defenders.defense:
            hit -= defenders.defense
            print("{} attacks {} for {} damage!".format(fighters.ID, defenders.ID, hit))
            d.damaged(hit)
        else:
            print("{} attacks {} but misses!".format(fighters.ID, defenders.ID,))
    elif hit > d.defense:
        hit -= d.defense
        print("{} attacks {} for {} damage!".format(fighters.ID, d.ID, hit))
        d.damaged(hit)
    else:
        print("{} attacks {} but misses!".format(fighters.ID, d.ID))



    
#GAMEPLAY
game_round = 0
while True:
    game_round += 1
    print("what are your orders Hive Mind")
    #orders = input().lower()
    orders = "attack"

    if orders == "attack":
        print("Who do you want to attack with?")
        #attacker = input()
        attacker = A2001
        if attacker in Ycaptains:
            print("who are you attacking them with?")
            #defender = input()
            defender = B2001
            if defender in Ecaptains:
                battle(attacker, defender)
                battle(defender, attacker)
                battle(attacker, defender)
                battle(defender, attacker)
                battle(attacker, defender)
                battle(defender, attacker)


    if game_round == 5:
        #check to see who had the most troops left
        if len(defender.sub) > len(attacker.sub):
            print(defender.ID, " wins!")
        elif len(defender.sub) == len(attacker.sub):
            print("it's a draw...")
        else:
            print(attacker.ID, " wins!")

        print("the surviving grunts are:")
        for i in B2001.sub:
            print(i.ID)
        for i in A2001.sub:
            print(i.ID)
        break
    
