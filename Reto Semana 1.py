# Reto Semana 1
# 1: el cliente compra 1 pantalón de hombre código 123 por valor de $45000, una
#camisa manga corta código 345 por valor de $35000 y por último una camiseta Polo
#código 456 por valor de $27000.
#Caso 2: el cliente compra 3 camisetas cuello redondo  codigo 321 por valor de $12000 cada una,
#2 pares de medias tobilleras codigo 745 por valor de $3000 cada par.
import os


total_value = 0
cart = []
codes = {123: ['trousers', 45000], 345:['short sleeve t-shirt', 35000], 
456:['polo', 27000], 745: ['socks', 3000], 321:['round neck t-shirt', 3000], 0: ['exit', 0]}


#Unpack dictionary
def show_list():
    for code, (item, value) in codes.items():
        print(code, item)
        

show_list()

chosen_code = int(input('Please chooose the code for the desired item: '))

while chosen_code != 0:
    quantity = int(input('Please chooose the code for the quantity of the item: '))
    os.system('clear')
    show_list()
    if chosen_code not in codes:
        print("You must choose the code from an item of the list: ")
        chosen_code = int(input('Please chooose the code for your item: '))
        quantity = int(input('Please chooose the code for the quantity of the item: '))

    products = codes[chosen_code]
    cart  += products 
    item_value = cart[1] * quantity
    total_value += item_value 
    chosen_code = int(input('Please chooose the code for the desired item: '))
    os.system('clear')
    show_list()
os.system('clear')
print(f'The total value for the items you choose is ${total_value}')
    
    

