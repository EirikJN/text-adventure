lukehp = 3
proteinbar = 0
hp = 100
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
    global proteinbar
    if lukehp <= 1:
        print("du ødela luka! du er nå fri!")
        print("")    
        print("vil du ha en proteinbar?")
        asking = True
        while asking == True:
            valg = input("A: jaa B: nuh uh -> ")
            if valg == "A" or valg == "B":
                asking = False
            else:
                print("Du skrev feil i input, velg et av alternativene")
                print("")
    
        if valg == "A":
            print("nice")
            proteinbar += 1
            print("")
            print(f"du har nå {proteinbar} proteinbar(er)")
        elif valg == "B":
            pass

    else:    
        print("luka er bra sterk.. du sitter enda låst inne i vanen, prøv igjen")
        print("")
        van2()
    

def skall():
    global hp
    print("du kastet skallet ut av vinduet, en mann går forbi, ser skallet, men ser også en nøkkel! han låser opp vanen.")
    print("")
    print("du går ut av den, og innser at du er i The Backrooms..")



        

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

  

    