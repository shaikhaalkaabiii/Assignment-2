from guest import Guest

class Feedback:
    """Represents feedback provided by a guest after their stay."""

    def __init__(self, feedback_id, guest, rating, comments):
        """
        Initialize a Feedback object.

        feedback_id: Unique identifier for the feedback.
        guest: Guest object providing the feedback.
        rating: Rating given by the guest (1 to 5).
        comments: Comments provided by the guest.
        """
        self._feedback_id = feedback_id    # Private attribute
        self._guest = guest                # Private attribute
        self._rating = rating              # Private attribute
        self._comments = comments          # Private attribute

    # Getter methods
    def get_feedback_id(self):
        """Return the feedback's ID."""
        return self._feedback_id

    def get_rating(self):
        """Return the rating provided by the guest."""
        return self._rating

    def get_comments(self):
        """Return the comments provided by the guest."""
        return self._comments

    # Setter methods
    def set_rating(self, rating):
        """Set the rating provided by the guest."""
        try:
            if not 1 <= rating <= 5:
                raise ValueError("Rating must be between 1 and 5.")
            self._rating = rating
        except ValueError as e:
            print(f"Error: {e}")

    def __str__(self):
        """Return a string representation of the feedback."""
        return (f"Feedback ID: {self._feedback_id}, "
                f"Guest: {self._guest.get_name()}, "
                f"Rating: {self._rating}, Comments: {self._comments}")
