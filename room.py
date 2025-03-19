class Room:
    """Represents a room in the hotel."""

    def __init__(self, room_id, room_type, amenities, price_per_night):
        """
        Initialize a Room object.

        room_id: Unique identifier for the room.
        room_type: Type of the room (e.g., single, double, suite).
        amenities: List of amenities in the room.
        price_per_night: Price per night for the room.
        """
        self._room_id = room_id            # Private attribute
        self._room_type = room_type        # Private attribute
        self._amenities = amenities        # Private attribute
        self._price_per_night = price_per_night  # Private attribute
        self._is_available = True          # Private attribute, default value

    # Getter methods
    def get_room_id(self):
        """Return the room's ID."""
        return self._room_id

    def get_room_type(self):
        """Return the room's type."""
        return self._room_type

    def get_amenities(self):
        """Return the room's amenities."""
        return self._amenities

    def get_price_per_night(self):
        """Return the room's price per night."""
        return self._price_per_night

    def is_available(self):
        """Return the room's availability status."""
        return self._is_available

    # Setter methods
    def set_availability(self, status):
        """Set the room's availability status."""
        try:
            if not isinstance(status, bool):
                raise ValueError("Availability status must be a boolean (True or False).")
            self._is_available = status
        except ValueError as e:
            print(f"Error: {e}")

    def __str__(self):
        """Return a string representation of the room."""
        return (f"Room ID: {self._room_id}, Type: {self._room_type}, "
                f"Amenities: {', '.join(self._amenities)}, "
                f"Price per Night: ${self._price_per_night}, "
                f"Available: {self._is_available}")
