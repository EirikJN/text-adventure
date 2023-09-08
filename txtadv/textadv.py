hp = 100

def rom_1():
    global hp

    print("HP:", hp )

    print("Du står nå i rom 1")
    asking = True
    while asking == True:
        valg = input("A: ___ B: ___ -> ")
        if valg == "A" or valg == "B":
            asking = False
        else:
            print("Du skrev feil i input, velg et av alternativene")
 
    if valg == "A":
        rom_2()  
    elif valg == "B":
        rom_3()

def rom_2():
    global hp

    print("Du står nå i rom 2")
    hp -= 30
    print("HP: ", hp )

    asking = True
    while asking == True:
        valg = input("A: ___ B: ___ -> ")
        if valg == "A" or valg == "B":
            asking = False
        else:
            print("Du skrev feil i input, velg et av alternativene")
 
    if valg == "A":
        rom_1()  
    elif valg == "B":
        rom_3()

def rom_3():
    global hp

    print("Du står nå i rom 3")
    hp += 15
    print("HP:", hp )
    if hp <= 0:
        print("god natt")
        exit()

    asking = True
    while asking == True:
        valg = input("A: ___ B: ___ -> ")
        if valg == "A" or valg == "B":
            asking = False
        else:
            print("Du skrev feil i input, velg et av alternativene")
 
    if valg == "A":
        rom_1()  
    elif valg == "B":
        rom_2()

  

    