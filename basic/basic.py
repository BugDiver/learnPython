def is_even(num):
    if num%2 == 0:
        return True
    else:
        return False

def is_odd(num):
    if num%2 != 0:
        return True
    else:
        return False

def square(num):
    return num * num

def cube(num):
    return square(num) * num

def simple_interest(p ,r ,t):
    return (p * r * t) / 100

def sum_of_1_to_N(num):
    return (num * (num+1))/2

def greatest_between_three(n1 ,n2 ,n3):
    if (n1 >= n2 or n1 >=n3):
        return n1
    elif n2 >= n3:
        return n2
    else:
        return n3
def average_of_three(n1 ,n2 ,n3):
    return round(float(n1 +n2+n3)/3 ,2)
