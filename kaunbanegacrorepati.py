Questions = ["Who is the Prime Minister of India","What is the National Animal of India"]
Answer = ["Narendra Modi","Peacock"]
points = 0
print(Questions[0])
for i in range(0,2):
    print(Questions[i],"\n")
    Your_Answer = input("Your answer is ")
    if(Your_Answer == Answer[i] ):
        print("Your answer is correct\n")
        points = points + 1

    

print("Your point is ",points)

# print("Write any one of the option")
# print(Questions[0])
# print("[A] Narendra Modi                          [B] Manmohan Singh")
# print("[C] Indira Gandhi                          [D] Jawaharlal Nehru")
# if()