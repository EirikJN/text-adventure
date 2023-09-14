lukehp = 3

def van():

    print("")
    print("")
    print("Du har blitt kidnappet av Kanye West, og du blir forlatt i en van")
    print("")
    print("Der finner du et brekkhjern og et appelsinskall, Hva skal du gjøre?")
    print("")
    van2()  

def van2():
    global lukehp
    lukehp -= 1
    asking = True
    while asking == True:
        valg = input("A: slå bakluka med brekkhjernet B: kast appelsinskallet ut vinduet -> ")
        print("")
        if valg == "A" or valg == "B":
            asking = False
        else:
            print("Du skrev feil i input, velg et av alternativene")
            print("")
 
    if valg == "A":
        brekk()  
    elif valg == "B":
        skall()

def brekk():
    if lukehp <= 1:
        print("du ødela luka! du er nå fri!")
        print("")

    else:    
        print("luka er bra sterk.. du sitter enda låst inne i vanen, prøv igjen")
        print("")
        van2()
    

def skall():

    print("du kastet skallet ut av vinduet, en mann går forbi, ser skallet, men ser også en nøkkel! han låser opp vanen.")
    print("")
    print("du går ut av den, og innser at du er i The Backrooms..")
    print("")

    asking = True
    while asking == True:
        valg = input("A: ___ B: ___ -> ")
        if valg == "A" or valg == "B":
            asking = False
        else:
            print("Du skrev feil i input, velg et av alternativene")
            print("")
 
    if valg == "A":
        rom_1()  
    elif valg == "B":
        rom_2()

    print("HP: ", hp )
    if hp <= 0:
        print("god natt")
        exit()

def noe():
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

van()

  

    