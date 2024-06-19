from main import service_tickets
from view_tickets import tickets_list
def status_update():
    tickets_list()
    select_ticket = input("Which ticket do you want to close?\n").capitalize()
    service_tickets[f"{select_ticket}"]["Status"] = "Closed"