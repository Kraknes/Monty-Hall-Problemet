import random

rounds = 1000
doors_nr = 3
i = 0
ii = 0
riktig = 0

door_list = []
choose_list = []

# Lage klasse dør som kan ha premie og bli valgt
class door:
    def __init__(self, number, price):
        self.number = number
        self.price = price
        self.chosen = False
 
# Lage antall dører til problemet. Generelt er den 3, men her kan man leke.            
def create_doors(i):
    while i < doors_nr:
        door_list.append(door(i, False))
        i += 1
 
# Velger tilfeldig dør med premie av de tre dørene                
def door_price():
    door_w_price = random.randint(0, doors_nr-1)
    door_list[door_w_price].price = True
    prize_door = door_list[door_w_price]
    choose_list.append(prize_door)

    
# Velger tilfeldig dør som skal bli valgt. Kan ha premie eller ikke premie. 
def choose_door():
    chosen_door = random.randint(0, doors_nr-1)
    door_list[chosen_door].chosen = True
    choose_list.append(door_list[chosen_door])

# Velger den andre døra en den man valgte.     
def choose_second_door():
    prize = 0
    for door in choose_list:
        if door.chosen == True:
            door.chosen = False
        else:
            door.chosen = True
            if door.price == True:
                prize += 1
    return prize

# En del av itereringen for å nullstille parametere
def start_over():
    door_list.clear()

# Printe funksjon
def print_results():
    print()
    print()
    print("The Monty Hall Problem")
    print()
    print()
    print("Av " + str(doors_nr) +" dører, skal deltager velge en dør og så bytte dør for å få premie. Dette gjøres " + str(rounds) + " ganger for å opprette sannsynlighet.")
    print()
    print()
    print(str(antall_riktig) + " av " + str(rounds) + " var riktig av å bytte dør")
    print()
    print()
    print(str(antall_riktig/rounds * 100) + " % " + "av dørene hadde premie av å bytte dør")
    print()
    print()   
 
    

# while funksjon som kjører scripten   
while ii < rounds:
    create_doors(i)
    door_price()
    choose_door()
    choose_second_door()
    start_over()
    ii += 1

antall_riktig = choose_second_door()
print_results()


