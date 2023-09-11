question = [
    [
        "Who is the Prime Minister of Bharat","Narendra Modi","Jawaharlal Nehru","Manmohan Singh","Pratibha Patil"
        ],
    [
        "Who is the President of Bharat","Draupati Murmu","Pratibha Patel","nehru","Ravi"
        ],
    [
        "Who is the Prime Minister of Bharat","Narendra Modi","Jawaharlal Nehru","Manmohan Singh","Pratibha Patil"
        ],
    [
        "Who is the President of Bharat","Draupati Murmu","Pratibha Patel","nehru","Ravi"
        ],
    [
        "Who is the Prime Minister of Bharat","Narendra Modi","Jawaharlal Nehru","Manmohan Singh","Pratibha Patil"
        ],
    [
        "Who is the President of Bharat","Draupati Murmu","Pratibha Patel","nehru","Ravi"
        ],
    [
        "Who is the Prime Minister of Bharat","Narendra Modi","Jawaharlal Nehru","Manmohan Singh","Pratibha Patil"
        ],
    [
        "Who is the President of Bharat","Draupati Murmu","Pratibha Patel","nehru","Ravi"
        ]
    ]
money = 0
price = [1000,2000,3000,5000,10000,20000,35000,50000,120000,320000]
for i in range(0,len(question)):
    questions = question[i]
    print(f"\nPrize money for question {i+1} is {price[i]}\n{question[i][0]}")
    print(f'''A.{questions[1]}         B.{questions[2]}
              C.{questions[3]}       D.{questions[4]}''')
    reply = int(input("Enter your option as (1-4): "))
    if(reply == 1):
        print("Your answer is correct")

    else:
        print("Wrong answer")
        break

