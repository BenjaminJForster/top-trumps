print ("Welcome to Harry Potter Top Trumps")

#Player 1
print ("Player 1: Please enter the details on your card")
P1Charname = input("Enter the name of the character on the card: ")
P1MP = int(input("Enter number of magical points: "))
P1Strength = int(input("Enter number for strength: "))
print ("your card details are below:")
print("character: ", P1Charname)
print("Magical points: ", P1MP)
print("Strength: ", P1Strength)

#Player 2
print ("Player 2: Please enter the details on your card")
P2Charname = input("Enter the name of the character on the card: ")
P2MP = int(input("Enter number of magical points: "))
P2Strength = int(input("Enter number for strength: "))
print ("your card details are below:")
print("character: ", P2Charname)
print("Magical points: ", P2MP)
print("Strength: ", P2Strength)

if (P1MP > P2MP):
    print(P1Charname, "have the most magical points.")
    print(P1Charname, "wins a card.")
elif(P2MP > P1MP):
    print(P2Charname, "have the most magical points.")
    print(P2Charname, "wins a card.")
else:
    print(P1Charname, "and", P2Charname, "have equal magical points.")
    print(P1Charname, "and", P2Charname, "draw.")