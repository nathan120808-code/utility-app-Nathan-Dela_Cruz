#common dictionaries
venmach = {
    11 : ['Cheetos' , 3.0],
    12 : ['Doritos', 3.0], #this follows the following format = item code : item
    13 : ['Lays', 3.0],
    14 : ['Oman Chips', 3.0],
    15 : ['Bugles' ,3.0],
    21 : ['Apple',3.0],
    22 : ['Orange',3.0],
    23 : ['Pineapple',3.0],
    24 : ['Mango',3.0],
    25 : ['Mixed Berries',3.0],
    31 : ['Galaxy',3.0],
    32 : ['Snickers',3.0],
    33 : ['M&Ms',3.0],
    34 : ['Skittles',3.0],
    35 : ['KitKat',3.0],
    41 : ['Coca-Cola',3.0],
    42 : ['Fanta',3.0],
    43 : ['7UP',3.0],
    44 : ['Sprite',3.0],
    45 : ['Pepsi',3.0]
    }

def select_process():
    print(' ')
    print('Confirm your selection.')
    print(' ')
    print('Layout follows - [Item , Price]')
    user_input = str(input('Yes or No: '))
    
   
    if user_input.lower() == 'yes': #checks if the user answers yes before sending it into a loop
        while True: #infinite loop
            print('Please enter item code') 
            code_input = int(input('Code: ')) #prompts the user for item code
            try: #will try for variables located within the specific dictionary below
                item = venmach[code_input] #the code will try for keys based on the user input, it would then subtitue venmach_chips[code_input] with the key and key variable - they will act as values. 'Item' acts as the variable storing the two
                print(f'You have chosen {item}.')
                user_ask = str(input('Continue? (Yes or No): '))
                if user_ask.lower() == 'yes': #checks if the answer is yes
                        transaction_process()
                        break
                else:
                    print('Please select again.')
                    continue #loops back into asking 
            except KeyError: #this prevents the program from crashing if an invalid code is inputted - instead providing the prompt below
                print(f'Error the code is unavailable.')
    else:
        print('Would you like to re-order? (Yes or No)') #prompts the user if they would like to re-order
        re_order = str(input('Yes or No: ')) #prompts the user for an answer
        if re_order.lower() == 'yes': #checks if the answer is yes
            start_process() #starts from beginning
        else:
            print('Have a good day!') #ends the program
    

def transaction_process():
    print(' ')
    print(f'Item Info: 3 AED')
    print(' ')
    balance = 0
    
    while True:
        money = float(input('Please insert money: '))
        balance += money

        if balance == 3.0:
            print('Thank you, Enjoy!')
            break

        elif balance >= 3.0:
            print('Here is your change: ', balance - 3.0)
            print('Enjoy!')
            break
        else:
            print('Funds are insufficient')
            if balance != 3.0:
                continue
            else:
                print('Thank you, enjoy!')
                break
    continue_process()

def menu_chips(): #all the code below this function and other similar functions are just for printing the menu
    print(' ')
    print('Chips - 3 AED')
    print(' ')
    print('Cheetos - 11')
    print('Doritos - 12')
    print('Lays - 13')
    print('Oman Chips - 14')
    print('Bugles - 15')

    select_process() #calls upon the selection function


def menu_juice():
    print(' ')
    print('Juice - 2 AED')
    print(' ')
    apple = 21
    print('Apple - 21')
    orange = 22
    print('Orange - 22')
    pineapple = 23
    print('Pineapple - 23')
    mango = 24
    print('Mango - 24')
    mixberries = 25
    print('Mixed Berries - 25')

    select_process()

def menu_candy():
    print(' ')
    print('Candy - 3 AED')
    print(' ')
    galaxy = 31
    print('Galaxy Chocolate - 31')
    snickers = 32
    print('Snickers Chocolate - 32')
    mnms = 33
    print('M&Ms - 33')
    skittles = 34
    print('Skittles - 34')
    kitkat = 35
    print('Kit Kat - 35')

    select_process()


def menu_soda():
    print(' ')
    print('Soda - 3 AED')
    print(' ')
    coke = 41
    print('Coca-Cola - 41')
    fanta = 42
    print('Fanta - 42')
    sprite = 43
    print('Sprite - 43')
    sevenup = 44
    print('7UP - 44')
    pepsi = 45
    print('Pepsi - 45')

    select_process()     

def water_process():
    print(' ')
    print('Water - 1 AED')
    print(' ')
    balance = 0
    
    while True:
        money = float(input('Please insert money: '))
        balance += money

        if balance == 1.0:
            print('Thank you, Enjoy! (One item has been dispensed)')
            break

        elif balance >= 1.0:
            print('Here is your change: ', balance - 1.0)
            print('Enjoy! (One item has been dispensed)')
            break
        else:
            print('Funds are insufficient')
            if balance != 1.0:
                continue
            else:
                print('Thank you, enjoy! (One item has been dispensed)')
                break
    continue_process()          

def continue_process():
    print(' ')
    print('Would you like to purchase again?')
    print(' ')
    user_input = str(input('Yes or No: '))
    if user_input.lower() == 'yes':
        start_process()
    else:
        print('Thank you!')

def start_process():
    print(' ')
    print('Hello! Please select your choice of snack.')
    print(' ')
    list = ['chips','juices','candies','water']
    print('Chips | Juices | Sodas | Candies | Water') #prints vailable classification options
    choice = input('Please input: ') #prompts the user for their choice                                              

    while True:
        if  choice.lower() == 'chips': #checks if the either all the criteria below are met
            menu_chips()
            break
        elif choice.lower() == 'candies':
            menu_candy()
            break
        elif choice.lower() == 'juices':
            menu_juice()
            break
        elif choice.lower() == 'sodas':
            menu_soda()
            break
        elif choice.lower() == 'water':
            water_process()
            break

        else:
            print('Choice is not available.')
            break

start_process()