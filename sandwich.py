available_sandwiches = ['\ntuna', '\nham', '\ncheese', '\nvegetarian', '\nvegan', '\nprosciutto', '\nchicken', '\nbeef']
sandwich_orders = []
making_sandwiches = []
finished_sandwiches = []
missing_sandwiches = []

print('\nAvailable sandwiches: ', ''.join(available_sandwiches).title())

while True:

    y = str(input('\nPlease type in lowercase!\nIf we have all sandwiches available today write \'continue\''
                  '.\nAnd if not write only one at a time, sandwich that is missing today: ')).lower()

    if y == 'continue':
        break

    elif y not in str(available_sandwiches):
        print('\nPlease type the word in lowercase and/or correctly!')
        continue

    else:
        missing_sandwiches.append(y)


while True:

    missing = ', '.join(missing_sandwiches)
    if len(missing_sandwiches) > 0:
        print(f'\nToday we are not offering {missing.title()} sandwiches.\nThank you for understanding!')
    else:
        print('We currently have no orders.')

    while True:

        x = str(input("\nDo you have a new order?\nIf you don't, please enter 'no'."
                      "\nIf you do, please enter it here: ")).lower()

        if x == 'no':
            break

        elif x not in str(available_sandwiches):
            print(f'\nPlease type the word in lowercase and/or correctly!')
            continue

        elif x in missing_sandwiches:
            print(f'\nSorry, but we have run out of {x.title()} sandwiches. Please make another order.')

        else:
            sandwich_orders.append(x)

    print('\nOrders waiting:', ', '.join(sandwich_orders))
    sandwich = input('\nEnter current order: ').lower()

    if sandwich not in sandwich_orders:
        print('\nPlease type the word in lowercase and/or correctly!')

    while sandwich in missing_sandwiches:
        sandwich_orders.remove(sandwich)

        if sandwich not in sandwich_orders:
            print(f'\nSorry, but we have run out of {missing.title()}. Please make another order.')
            break

    if sandwich in sandwich_orders:
        making_sandwiches.append(sandwich)
        sandwich_orders.remove(sandwich)
        print(f'\n{sandwich.title()} sandwich will be delivered.')

        while True:

            making = ''.join(making_sandwiches)
            msg = input(f'\nIs {making.title()} sandwich done?\nPlease enter yes or no: ').lower()

            if msg == 'yes':
                finished_sandwiches.append(sandwich)
                making_sandwiches.remove(sandwich)
                break

            else:
                print(f'\nPlease finish current {making.title()} sandwich firs!')
                continue

    finished = ', '.join(finished_sandwiches)
    orders = ', '.join(sandwich_orders)

    if len(finished_sandwiches) > 0:
        print(f'\nWe have finished {finished.title()} sandwiches and we still have to make\n'
              f'{orders.title()} sandwiches.')

    continue
