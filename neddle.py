haystack = "hello"
neddle = 'll'
print("Start\n")

i = 0
while(i<len(haystack)):
    print(i)
    if(haystack[i] == 'l'):
        print(i)
        break
    else:
        continue
    i= i+1

 