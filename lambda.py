double = lambda x:x*2

print(double(3))

def appl(fx,value):
    return fx(value)

l = [1,2,4,3,5]
# newl=[]
# for item in l:
#     newl.append(appl(lambda x:x*x*x,item))
# print(newl)

newl = list(map(lambda x:x*x*x,l))
print(newl)
