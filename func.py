import operator
x=str(input("please enter a string "))
def most_frequent(string):
    d=dict()
    for k in string:
        if k not in d:
            d[k] = 1
        else:
            d[k] +=1
    return d
z = most_frequent(x)

sorted_z = dict(sorted(z.items(),key=operator.itemgetter(1),reverse=True))
for i in sorted_z:
    print(i," : ",sorted_z[i])
