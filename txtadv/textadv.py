lukehp = 3
proteinbar = 0
van_nøkkel = 0
def van():

    print("")
    print("")
    print("Du har blitt kidnappet av Kanye West, og du blir forlatt i en van")
    print("")
    print("Der finner du et brekkhjern og et appelsinskall, Hva skal du gjøre?")
    
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
        print("du går ut av den, og innser at du er i The Backrooms..")
        print("")    

        pr0teinbar()

        backrooms_intro()

    else:    
        print("luka er bra sterk.. du sitter enda låst inne i vanen, prøv igjen")
        van2()
    

def skall():
    global proteinbar
    print("du kastet skallet ut av vinduet, en mann går forbi, ser ned på skallet som ligger på bakken")
    print("men ser også en nøkkel som ligger rett ved siden av den! han låser opp vanen.")
    print("du går ut av den, og innser at du er i The Backrooms..")
    print("")

    backrooms_intro()


def pr0teinbar():
    global proteinbar
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
            print("")
            print("nice")
            proteinbar += 1
            
            if proteinbar == 1:
                print(f"du har {proteinbar} proteinbar")
                print("")
            
            else:
                pass

        elif valg == "B":
            pass
        
def backrooms_intro():
    print("du ser tre ganger, du må velge en av de")
    print("gang 1 er veldig mørk, ser ikke ut til å ha en ende..")
    print("gang 2 er lyst opp av røde lyspaneler i taket")
    print("gang 3 er lyst opp av grønn-gule lyspaneler i taket, ser ut til å være et skap lengre inn i gangen")
    print("")
    print("hvilken velger du?")
    backrooms()

def backrooms():
    asking = True
    while asking == True:
        valg = input("A: gang 1 B: gang 2 C: gang 3 -> ")
        print("")
        if valg == "A" or valg == "B" or valg == "C":
            asking = False
        else:
            print("Du skrev feil i input, velg et av alternativene")
            print("")
 
    if valg == "A":
        gang_1()  
    if valg == "B":
        gang_2()
    if valg == "C":
        gang_3()

def gang_1():
    print("du går inn i gangen, tilslutt blir det så mørkt at du ikke ser noe, men du følger veggen videre")
    print("så ser du en slutt på gangen")
    print("når du kommer frem, så innser du at du har gått i en sirkel.. du er tilbake til der du startet")
    print("")
    backrooms()


def gang_2():
    global van_nøkkel
    van_nøkkel += 1
    print("du går inn i gang 2, her finner du nøkkelen til vanen!")
    print("men ellers er det en blindvei, du drar tilbake ")
    backrooms()


def gang_3():
    print("du går lengre inn i gangen, plutselig blir alle lysene rød")
    print("du nærmer deg skapet, vil du gå bort til det?")
    print("")
    asking = True
    while asking == True:
        valg = input("A: gå til skapet B: gå videre -> ")
        if valg == "A" or valg == "B":
            asking = False
        else:
            print("Du skrev feil i input, velg et av alternativene")
            print("")

    if valg == "A":
        skap()  
    elif valg == "B":
        gå_videre()


def skap():
    print("det var veldig lurt, for bare sekunder senere hører du en høy lyd, du gjemmer deg i skapet, like etter går det et monster forbi")
    print("")
    van_finn()


def gå_videre():
    global proteinbar
    print("du går videre, men bare noen få sekunder senere hører du dunking rett over deg")
    print("like etter faller det en plate ned fra taket, og samtidig hopper det et monster ned rett forran deg")
    print("")
    print("hva vil du gjøre??")
    asking = True
    while asking == True:
        valg = input("A: gi bro en klem B: LØP -> ")
        if valg == "A" or valg == "B":
            asking = False
        else:
            print("Du skrev feil i input, velg et av alternativene")
            print("")

    if valg == "A":
        klem()  
    elif valg == "B":
        løp()


def løp():
    print("du løper så fort du bare klarer, men monsteret tar deg snart igjen!")
    print("vil du spise en proteinbar?")
    if proteinbar == 1:
        print(f"du har {proteinbar} proteinbar")
        print("")
        asking = True
        while asking == True:
            valg = input("A: spis den B: ekke sulten -> ")
        if valg == "A" or valg == "B":
            asking = False

        else:
            print("Du skrev feil i input, velg et av alternativene")
            print("")

    if valg == "A":
        spist()  
    elif valg == "B":
        ikke_sulten()
            
    else:
        print("du har dessverre ingen proteinbarer..")
        print("monsteret tok deg igjen, og du ble knaska på")
        quit


def spist():
    print("smart valg, nå har du energien til å løpe fra den!")


def van_finn():
    print("nå ser du vanen igjen!")
    print("du går til vanen, og innser at den er låst igjen")
    if van_nøkkel >= 1:
        print("du har en nøkkel!")
        print("")
        asking = True
        while asking == True:
            valg = input("trykk A for å bruk e den -> ")
        if valg == "A":
            asking = False

        else:
            print("Du skrev feil i input, velg et av alternativene")
            print("")

    if valg == "A":
            escape()  
                
    else:
        print("du har dessverre ikke en nøkkel..")
        print("du er låst inne i The Backrooms for alltid...")
        quit


def ikke_sulten():
    print("oisann, monsteret tok deg igjen, den var ikke interessert i å bli venner! god natt")
    quit

def klem():
    print("uffda, det endte ikke bra, du døde")
    quit

def escape():
    print("yep")


van()