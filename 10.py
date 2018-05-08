def oszthato(n):
    number=1
    while True:
        for oszto in range(1,n+1):
            if number%oszto!=0:
                break
        else:
            return number
        number+=1
print(oszthato(20))