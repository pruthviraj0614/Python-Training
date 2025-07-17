<<<<<<< Updated upstream
def generate_tickets_number(airline, src, dest, number_passengers):
    tickets = []
    src_code = src[:3].upper()
    dest_code = dest[:3].upper()
    
    for i in range(101, 101 + number_passengers):
        ticket = f"{airline}:{src_code}:{dest_code}:{i}"
        tickets.append(ticket)
        
    return tickets

airline = "AI"
src = input("Enter the source: ")
dest = input("Enter the destination: ")

num_passengers = int(input("Enter the number of passengers: "))

ticket_numbers = generate_tickets_number(airline, src, dest, num_passengers)

print("\nGenerated Tickets:")
for ticket in ticket_numbers:
    print(ticket)
=======
def generate_tickets_number(airline, src, dest, number_passengers):
    tickets = []
    src_code = src[:3].upper()
    dest_code = dest[:3].upper()
    
    for i in range(101, 101 + number_passengers):
        ticket = f"{airline}:{src_code}:{dest_code}:{i}"
        tickets.append(ticket)
        
    return tickets

airline = "AI"
src = input("Enter the source: ")
dest = input("Enter the destination: ")

num_passengers = int(input("Enter the number of passengers: "))

ticket_numbers = generate_tickets_number(airline, src, dest, num_passengers)

print("\nGenerated Tickets:")
for ticket in ticket_numbers:
    print(ticket)
>>>>>>> Stashed changes
