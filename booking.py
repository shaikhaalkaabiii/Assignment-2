from guest import Guest
from room import Room

class Booking:
    """Represents a booking made by a guest."""

    def __init__(self, booking_id, guest, room, check_in_date, check_out_date):
        """
        Initialize a Booking object.

        booking_id: Unique identifier for the booking.
        guest: Guest object making the booking.
        room: Room object being booked.
        check_in_date: Check-in date for the booking.
        check_out_date: Check-out date for the booking.
        """
        self._booking_id = booking_id      # Private attribute
        self._guest = guest                # Private attribute
        self._room = room                  # Private attribute
        self._check_in_date = check_in_date  # Private attribute
        self._check_out_date = check_out_date  # Private attribute
        self._total_cost = self.calculate_total_cost()  # Private attribute

    # Getter methods
    def get_booking_id(self):
        """Return the booking's ID."""
        return self._booking_id

    def get_guest(self):
        """Return the guest associated with the booking."""
        return self._guest

    def get_room(self):
        """Return the room associated with the booking."""
        return self._room

    def get_total_cost(self):
        """Return the total cost of the booking."""
        return self._total_cost

    # Helper method
    def calculate_total_cost(self):
        """Calculate the total cost of the booking."""
        try:
            if not self._room.is_available():
                raise ValueError("Room is not available for booking.")
            nights = (self._check_out_date - self._check_in_date).days
            return nights * self._room.get_price_per_night()
        except ValueError as e:
            print(f"Error: {e}")
            return 0

    def __str__(self):
        """Return a string representation of the booking."""
        return (f"Booking ID: {self._booking_id}, Guest: {self._guest.get_name()}, "
                f"Room: {self._room.get_room_type()}, "
                f"Check-In: {self._check_in_date}, Check-Out: {self._check_out_date}, "
                f"Total Cost: ${self._total_cost}")
