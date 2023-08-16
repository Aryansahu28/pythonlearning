import time
timehour = int(time.strftime("%H"))
timemin = time.strftime("%M")
timesecs = time.strftime("%S")

if(timehour>5 and timehour < 12):
    print("Good Morning Sir ")

elif(timehour>12 and timehour<=4):
    print("Good Afternoon Sir")

else:
    print("Good Night")