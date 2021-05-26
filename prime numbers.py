
def prime_num(ls: list) -> list:
    """
    Function that returns the prime numbers of a set,
    you must choose the range. A is the lowest value 
    of the list and b the highest value"""
    
    prime = []
    for num in ls:
        contador = 0
        for i in range(1, num + 1):         
            if num % i == 0:
                contador += 1
        if contador == 2:
            prime.append(num)
    print(prime)


a = 1
b = int(input("Please enter the value for b: "))
ls = [i for i in range(a, b + 1)]
prime_num(ls)



