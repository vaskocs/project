def convert(list,b1,b2):
    number=0
    helyiertek=1
    for i in range(len(list)-1,-1,-1):
        if list[i]>=b1:
            print("Nem jó szám")
            return None
        number+=list[i]*helyiertek
        helyiertek*=b1
    list2=[]
    while number!=0:
        list2.append(number%b2)
        number//=b2
    list2.reverse()
    return list2
print(convert([1,9],8,2))