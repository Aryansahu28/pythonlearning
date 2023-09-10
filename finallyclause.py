def func1():
    try:
        lst = [1,3,5,2]
        i = int(input("Enter the index: "))
        print(lst[i])
        return 1

    except:
        print("Some error occurred")
        return 0

    finally:
        print("I am the one who excetutes everytime whatever the circumstances")
    # print("I am will be executed")


x = func1()
print(x)
