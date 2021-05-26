# 3x^2 - 5x +1

def cuad_functions(a: int, b: int, c: int)  -> float:
    """
    Funtion that will help you solve cuadratic equations, 
    a is the value that goes with the x^2, 
    b is the value that goes with x,
    c is the value that does not have an x next to it.
    This will return the root of the cuadratic equation
    """
    root_1 = (- b + (b**2 - 4 * a * c)**0.5)/(2 * a)
    root_2 =  (- b - (b**2 - 4 * a * c)**0.5)/(2 * a)
    
    print(root_1, root_2)


print('This is a program to help you solve cuadratic equations, please enter the following paramaters: a, b c')
a = int(input('Please enter the value for a: '))
b = int(input('Please enter the value for b: '))
c = int(input('Please enter the value for c: '))


cuad_functions(a, b, c)



