# Seat Reservation System 
seats = ["Empty"] * 40     # 40 seats 
PRICE = 250                # Price per ticket
ROUTE = "Hyderabad → Warangal"



def show_seats():
    print("\nBus Seating Layout (10 rows, 4 seats each):")
    print("X = Booked   O = Empty\n")
    print("Format: [Seat Number] [Availability]\n")
    

    for i in range(0, 40, 4):   # 4 seats per row
        # Seat 1
        if seats[i] != "Empty":
          a = "X"
        else:
          a = "O"
        a_num = i + 1

        # Seat 2
        if seats[i+1] != "Empty":
          b = "X"
        else:
          b = "O"
        b_num = i + 2

        # Seat 3
        if seats[i+2] != "Empty":
          c = "X"
        else:
          c = "O"
        c_num = i + 3

        # Seat 4
        if seats[i+3] != "Empty":
          d = "X"
        else:
          d = "O"
        d_num = i + 4

        print(f"Row {(i//4)+1}:  [{a_num}] [{a}]   [{b_num}] [{b}]   [{c_num}] [{c}]   [{d_num}] [{d}]")
    



def reserve_seats():
    print(f"\nRoute: {ROUTE}")
    print(f"Ticket Price: ₹{PRICE}\n")

    count = int(input("How many seats do you want to book? "))
    if count>40 or count<1:
       print("invalid count")
    if count>3:
        total_cost = (count * PRICE)
        discount = total_cost * 0.1         # for 10% discount
        total_cost = total_cost - discount
    else:
        total_cost = count * PRICE          # No discount
        
    for i in range(count):
        seat_no = int(input("Enter seat number (1-40): "))

        if seat_no < 1 or seat_no > 40:
            print("Invalid seat number!")
            continue

        if seats[seat_no-1] != "Empty":
            print("Seat already booked!")
            continue

        bookings_list = []
        name = input("Enter passenger name: ")
        seats[seat_no-1] = name
        bookings_list += name
        print(f"Seat {seat_no} booked successfully!\n")
    if count>3:
        print("Congratulation for claiming Family Discount of 10% on Total Price")
        print(f"Total Price for {count} tickets: ₹{total_cost}\n")
    else:
        print(f"Total Price for {count} tickets: ₹{total_cost}\n")



def cancel_seat():
    seat_no = int(input("Enter seat number to cancel (1-40): "))

    if seat_no < 1 or seat_no > 40:
        print("Invalid seat number!")
    elif seats[seat_no-1] == "Empty":
        print("Seat is already empty!")
    else:
        seats[seat_no-1] = "Empty"
        print(f"Reservation cancelled for seat number {seat_no}")


def main():
    while True:
        print("\n--- BUS SEAT RESERVATION SYSTEM ---")
        print("Welcome to PrimePath Travels")
        print(f"Route: {ROUTE} | Ticket Price: ₹{PRICE}")
        print("1. View Seats")
        print("2. Reserve Seats")
        print("3. Cancel Seat")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            show_seats()
        elif choice == 2:
            reserve_seats()
        elif choice == 3:
            cancel_seat()
        elif choice == 4:
            print("Thank you for Visiting, Have a Great day! ")
            break
        else:
            print("Invalid choice!")


main()