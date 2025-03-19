from booking import Booking

class Invoice:
    """Represents an invoice for a booking."""

    def __init__(self, invoice_id, booking, payment_method):
        """
        Initialize an Invoice object.

        invoice_id: Unique identifier for the invoice.
        booking: Booking object associated with the invoice.
        payment_method: Payment method used for the invoice.
        """
        self._invoice_id = invoice_id      # Private attribute
        self._booking = booking            # Private attribute
        self._payment_method = payment_method  # Private attribute

    # Getter methods
    def get_invoice_id(self):
        """Return the invoice's ID."""
        return self._invoice_id

    def get_booking(self):
        """Return the booking associated with the invoice."""
        return self._booking

    def get_payment_method(self):
        """Return the payment method used for the invoice."""
        return self._payment_method

    def __str__(self):
        """Return a string representation of the invoice."""
        return (f"Invoice ID: {self._invoice_id}, "
                f"Booking ID: {self._booking.get_booking_id()}, "
                f"Total Cost: ${self._booking.get_total_cost()}, "
                f"Payment Method: {self._payment_method}")
