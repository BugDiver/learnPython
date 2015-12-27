def gcd(n1 ,n2):
    rem = n2%n1
    while rem!=0:
        n2 = n1
        n1 = rem
        rem = n2 % n1
    return n1

def lcm(n1, n2):
    return (n1 * n2) / gcd(n1 ,n2)

def compound_interest(p ,r ,t):
    ammount = p
    for i in range(t):
        ammount += ((ammount * r) /100)
    return ammount - p

def factorial(num):
    fact  = 1
    for num in range(1,num+1):
        fact = fact * num
    return fact

def fibonacci(num):
    n1 = 0
    n2 = 1
    fibno = n1+n2
    if num==1:
        return n1
    elif num==2:
        return n2
    else:
        for i in range(3,num):
            n1 = n2
            n2 = fibno
            fibno = n1+n2
            print (n1 ,n2 ,fibno)
    return fibno
