# Import necessary classes and modules
from guest import Guest
from room import Room
from booking import Booking
from invoice import Invoice
from loyalty_program import LoyaltyProgram
from feedback import Feedback
from guest_service import GuestService
from datetime import datetime

# Main Program
if __name__ == "__main__":
    try:
        # Create a guest
        guest1 = Guest(1, "Shaikha Alkaabi", "Shaikha.j2005@gmail.com")
        print("Guest Details:")
        print(guest1)
        print()

        # Create a room
        room1 = Room(101, "Double", ["Free Breakfast", "Swimming Pool"], 120.0)
        print("Room Details:")
        print(room1)
        print()

        # Create a booking
        check_in = datetime(2023, 5, 15)  # Check-in date: May 15, 2023
        check_out = datetime(2023, 5, 20)  # Check-out date: May 20, 2023
        booking1 = Booking(1, guest1, room1, check_in, check_out)
        print("Booking Details:")
        print(booking1)
        print()

        # Create an invoice
        invoice1 = Invoice(1, booking1, "Credit Card")
        print("Invoice Details:")
        print(invoice1)
        print()

        # Add loyalty points
        loyalty_program1 = LoyaltyProgram(1, guest1)
        loyalty_program1.earn_points(100)  # Add 100 loyalty points
        print("Loyalty Program Details:")
        print(loyalty_program1)
        print()

        # Submit feedback
        feedback1 = Feedback(1, guest1, 5, "Excellent stay. I loved it.")
        print("Feedback Details:")
        print(feedback1)
        print()

        # Request guest service
        service1 = GuestService(1, "Housekeeping", datetime.now())
        service1.set_status("In Progress")  # Update service status
        print("Guest Service Details:")
        print(service1)

    except Exception as e:
        print(f"An error occurred: {e}")
