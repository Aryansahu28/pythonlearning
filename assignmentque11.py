x = input("Enter the card name: ")

if(str(x) == "Ace of Spade"):
    print("Lucky one")
    
elif(x == "Queen of Diamond"):
    print("Lucky one")
    
elif(x == "King of Diamond"):
    print("Lucky one")

elif(x[len(x)-8:]=="of Heart"):
    print("Lucky one")

elif(x[0]=="7"):
    print("Lucky one")

else:
    print("Better luck next time")