class GuestService:
    """Represents additional services requested by guests."""

    def __init__(self, service_id, service_type, request_time):
        """
        Initialize a GuestService object.

        service_id: Unique identifier for the service.
        service_type: Type of service requested (e.g., housekeeping, room service).
        request_time: Time when the service was requested.
        """
        self._service_id = service_id      # Private attribute
        self._service_type = service_type  # Private attribute
        self._request_time = request_time  # Private attribute
        self._status = "Pending"           # Private attribute, default value

    # Getter methods
    def get_service_id(self):
        """Return the service's ID."""
        return self._service_id

    def get_service_type(self):
        """Return the type of service requested."""
        return self._service_type

    def get_status(self):
        """Return the status of the service."""
        return self._status

    # Setter methods
    def set_status(self, status):
        """Set the status of the service."""
        try:
            if status not in ["Pending", "In Progress", "Completed"]:
                raise ValueError("Invalid status. Must be 'Pending', 'In Progress', or 'Completed'.")
            self._status = status
        except ValueError as e:
            print(f"Error: {e}")

    def __str__(self):
        """Return a string representation of the service."""
        return (f"Service ID: {self._service_id}, "
                f"Type: {self._service_type}, "
                f"Request Time: {self._request_time}, "
                f"Status: {self._status}")
