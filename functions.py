import json


def unique_id():
    file = open('clients.json', 'r')
    clients_to_dict = json.load(file)
    file.close()

    id_list = []
    for i in clients_to_dict:
        id_list.append(i)
    id_list.sort()
    try:
        id = int(id_list[-1]) + 1
    except:
        id = 1
    return id


def add_client():
    file = open('clients.json', 'r')
    clients_dict = json.load(file)
    file.close()

    new_id = unique_id()
    client = {
        'name': input('First name and Name:\n> '),
        'telephone': input('Phone number:\n> '),
        'city': input('City:\n> '),
        'balance': 0
    }
    clients_dict[new_id] = client
    new_client_json = json.dumps(clients_dict, indent=4)

    write_json_file = open('clients.json', 'w')
    write_json_file.write(new_client_json)
    write_json_file.close()


def check_clients():
    file = open('clients.json', 'r')
    clients_dict = json.load(file)
    file.close()
    print('*' * 30)
    print('\tClients:')
    for i in clients_dict:
        print(f'\t{i}. {clients_dict[i]["name"]} - tel:{clients_dict[i]["telephone"]} ')
    print('*' * 30)
    while True:
        option = input('Please select a client or type EXIT to return to main menu:\n> ')

        if option.lower() == 'exit':
            break
        elif option not in clients_dict:
            print('Please select a valid ID\n')
            continue
        else:
            print('-' * 50)
            print(f'Name: {clients_dict[option]["name"]}')
            print(f'Phone number: {clients_dict[option]["telephone"]}')
            print(f'City: {clients_dict[option]["city"]}')
            print(f'Balance: {clients_dict[option]["balance"]}')
            print('-' * 50)
            break

def client_balance():
    json_client_file = open('clients.json', 'r')
    client_dict = json.load(json_client_file)
    json_client_file.close()
    for i in client_dict:
        print(f'\t{i}. {client_dict[i]["name"]} - tel:{client_dict[i]["telephone"]} ')

    while True:
        client_select = input('\nEnter client ID or Exit to return to main menu:\n> ')
        print('*' * 50)
        if client_select.lower() == 'exit':
            break
        elif client_select not in client_dict:
            print('Invalid ID.')
            continue
        else:
            print(f'Current balance for "{client_dict[client_select]["name"]}":\n-- {client_dict[client_select]["balance"]}$ --')
            while True:
                options = ['1. New balance', '2. Exit']
                print('Options')
                for i in options:
                    print(i)
                option = int(input('Select an option:\n> '))
                if option == 1:
                    try:
                        edit_balance = int(input('Enter new balance:\n'))
                    except:
                        print('Please input a valid number')
                        continue

                    client_dict[client_select]["balance"] = edit_balance
                    update_client_json = open('clients.json', 'w')
                    update_client_json.write(json.dumps(client_dict, indent=4))
                    update_client_json.close()
                    print('Balance updated...')
                else:
                    break
            break

