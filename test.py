def soda_process():
    print(' ')
    print('Soda - 3 AED')
    print(' ')
    input = int(input('Enter item code: '))
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

