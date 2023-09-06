print("Det er en brann i huset, som vokser fort, men du er låst inne,")
print("hva skal du gjøre? A: Finne nøkkelen, eller B: Bryte opp døra")

valg = input("A eller B -> ")

if valg == "A":
    print("Nøkkelen")

if valg == "B":
    print("correct")
    print("A B")
    valg = input("A eller B -> ")

    if valg == "A":
        print("correct")

    if valg == "B":
        print("incorrect")

