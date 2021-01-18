import reports
from menu import menu
import functions


print('-' * 30)
print('Welcome to PAUL - BANK')
print('-' * 30)
while True:
    print('Menu:')
    print('*' * 30)
    for i in menu:
        print(i)
    print('*' * 30)
    try:
        option = int(input('Please select an option:\n> '))
        if option == 1:
            functions.add_client()
        elif option == 2:
            functions.check_clients()
        elif option == 3:
            functions.client_balance()
        elif option == 4:
            reports.report()
        elif option == 5:
            print('Program ended.')
            break
        else:
            print('Select valid option.')
            continue
    except:
        print('Invalid option')
        continue