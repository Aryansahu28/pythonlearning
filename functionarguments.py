def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i

    print(sum/len(numbers))

average(3,5,8)

