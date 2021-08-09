print("hello world")


def making_money(string):
    total = 0

    for count in range(6):
        total += count * string
    return total


print(making_money(5))

def making_money2(string):
    var=[]
    total=0
    for count in range(string):
        total+=count*string
        var.append(total)
    return var

print (making_money2(10))