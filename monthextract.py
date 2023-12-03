
birthday={'Joey':"22/10/2002",'Sunita':"19/03/2003",'Ravi':'11/04/2001','Suresh':'23/02/2004'}
def birthday_month(x):
    DOB = (birthday[x]) 
    month = DOB.split("/")
    print(month[1])

name = input("Enter your name : ")
birthday_month(name)