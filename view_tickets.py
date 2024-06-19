from main import service_tickets
def tickets_list():
        for ticket, details in service_tickets.items():
            print(f"{ticket}: {details['Issue']}, {details['Status']}, {details['Customer']}")
        while True:
            sort = input("Do you want to sort the list by status? Y/N\n").lower()
            if sort == "y" or "yes":
                sorted_tickets = dict(sorted(service_tickets.items(), key=lambda item: item[1]['Status']))
                for ticket, details in sorted_tickets.items():
                    print(f"{ticket}: {details['Issue']}, {details['Status']}, {details['Customer']}")
                    return
            elif sort == "n" or "no":
                return
            else:
                print("You didn't type a valid input. Try again after pressing 'enter'.\n")