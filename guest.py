class Guest:
    """Represents a guest staying at the hotel."""

    def __init__(self, guest_id, name, contact):
        """
        Initialize a Guest object.

        guest_id: Unique identifier for the guest.
        name: Name of the guest.
        contact: Contact information of the guest.
        """
        self._guest_id = guest_id  # Private attribute
        self._name = name          # Private attribute
        self._contact = contact    # Private attribute
        self._loyalty_points = 0   # Private attribute, default value

    # Getter methods
    def get_guest_id(self):
        """Return the guest's ID."""
        return self._guest_id

    def get_name(self):
        """Return the guest's name."""
        return self._name

    def get_contact(self):
        """Return the guest's contact information."""
        return self._contact

    def get_loyalty_points(self):
        """Return the guest's loyalty points."""
        return self._loyalty_points

    # Setter methods
    def set_name(self, name):
        """Set the guest's name."""
        self._name = name

    def set_contact(self, contact):
        """Set the guest's contact information."""
        self._contact = contact

    def add_loyalty_points(self, points):
        """Add loyalty points to the guest's account."""
        try:
            if points < 0:
                raise ValueError("Loyalty points cannot be negative.")
            self._loyalty_points += points
        except ValueError as e:
            print(f"Error: {e}")

    def __str__(self):
        """Return a string representation of the guest."""
        return (f"Guest ID: {self._guest_id}, Name: {self._name}, "
                f"Contact: {self._contact}, Loyalty Points: {self._loyalty_points}")
