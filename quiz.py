print("welcome to my computer quiz")

playing = input("do you want to play? ")

if playing != "yes":
    quit()

print("okay! Let's play :)")

answer = input("who is king of cricket? ")
if answer == "virat kohli":
    print("correct")
else:
    print("incorrect")

answer = input("who is god of cricket? ")
if answer == "sachin tendulkar":
    print("correct")
else:
    print("incorrect")

answer = input("how many centuries scored by sachin? ")
if answer == "100":
    print("correct")
else:
    print("incorrect")
    
