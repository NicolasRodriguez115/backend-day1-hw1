from main import service_tickets
from main import counter
def new_ticket():
    global counter
    customer = input("What's the name of the customer?\n").capitalize()
    issue = input("Write a brief description of your issue\n").capitalize()
    status = "Open"
    service_tickets[f"Ticket{counter}"] = {"Customer": f"{customer}", "Issue": f"{issue}", "Status": f"{status}"}
    counter += 1 
    