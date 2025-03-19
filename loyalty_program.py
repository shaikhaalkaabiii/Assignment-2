from guest import Guest

class LoyaltyProgram:
    """Represents the loyalty rewards program for guests."""

    def __init__(self, program_id, guest):
        """
        Initialize a LoyaltyProgram object.

        program_id: Unique identifier for the loyalty program.
        guest: Guest object associated with the loyalty program.
        """
        self._program_id = program_id      # Private attribute
        self._guest = guest                # Private attribute
        self._points = 0                   # Private attribute, default value

    # Getter methods
    def get_program_id(self):
        """Return the loyalty program's ID."""
        return self._program_id

    def get_points(self):
        """Return the loyalty points earned by the guest."""
        return self._points

    # Setter methods
    def earn_points(self, points):
        """Add loyalty points to the guest's account."""
        try:
            if points < 0:
                raise ValueError("Loyalty points cannot be negative.")
            self._points += points
            self._guest.add_loyalty_points(points)
        except ValueError as e:
            print(f"Error: {e}")

    def __str__(self):
        """Return a string representation of the loyalty program."""
        return (f"Loyalty Program ID: {self._program_id}, "
                f"Guest: {self._guest.get_name()}, "
                f"Points: {self._points}")
