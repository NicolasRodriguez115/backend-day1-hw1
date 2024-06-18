from main import service_tickets
def tickets_list():
    for ticket, details in service_tickets.items():
        print(f"{ticket}: {details}")