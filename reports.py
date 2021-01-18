from reportlab.pdfgen.canvas import Canvas
from datetime import date
import json
today = date.today()


def report():
    print('Select client:')
    print('*' * 50)

    json_client_file = open('clients.json','r')
    client_dict = json.load(json_client_file)
    json_client_file.close()

    for i in client_dict:
        print(f"{i}.{client_dict[i]['name']}")
    print('*' * 50)

    while True:
        option = input('Please select a client or type Exit to return to main menu:\n> ')

        if option.lower() == 'exit':
            break
        elif option not in client_dict:
            print('Please try again, ID is invalid')
            continue
        else:
            canvas = Canvas(f'pdf_files/{client_dict[option]["name"]}.pdf')
            canvas.setFont("Times-Roman", 18)
            canvas.drawString(20,800,"Acount Statement:")
            canvas.drawString(20, 780, "*" * 50)
            canvas.drawString(20, 760, f"{today}")
            canvas.drawString(20, 740, f"Name: {client_dict[option]['name']}")
            canvas.drawString(20, 720, f"Telephone: {client_dict[option]['telephone']}")
            canvas.drawString(20, 700, f"City: {client_dict[option]['city']}")
            canvas.drawString(20, 680, f"Balance: {client_dict[option]['balance']}")
            canvas.drawString(20, 660, "*" * 50)
            canvas.drawString(400,100, 'PAUL BankApp')
            canvas.save()
            print('File has been generated.')
            break