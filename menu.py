from new_ticket import new_ticket
from update_status import status_update
from view_tickets import tickets_list
import os
def menu():
    while True:
        print('''
        1. Open a new service ticket.
        2. Update the status of a ticket.
        3. See all tickets
        4. Quit
        ''')
        user_input = input("")
        if user_input == "1":
            os.system("cls")
            new_ticket()
        elif user_input == "2":
            os.system("cls")
            status_update()
        elif user_input == "3":
            os.system("cls")
            tickets_list()
        elif user_input == "4":
            break
        else:
            input("You've not entered a valid input. Press 'enter' to try again\n ")
