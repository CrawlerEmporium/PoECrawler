class FeCrawlerException(Exception):
    """A base exception class."""

    def __init__(self, msg):
        super().__init__(msg)


class InvalidArgument(FeCrawlerException):
    """Raised when an argument is invalid."""
    pass


class EvaluationError(FeCrawlerException):
    """Raised when a cvar evaluation causes an error."""

    def __init__(self, original, expression=None):
        super().__init__(f"Error evaluating expression: {original}")
        self.original = original
        self.expression = expression


class SelectionException(FeCrawlerException):
    """A base exception for message awaiting exceptions to stem from."""
    pass


class NoSelectionElements(SelectionException):
    """Raised when get_selection() is called with no choices."""

    def __init__(self, msg=None):
        super().__init__(msg or "There are no choices to select from.")


class SelectionCancelled(SelectionException):
    """Raised when get_selection() is cancelled or times out."""

    def __init__(self):
        super().__init__("Selection timed out or was cancelled.")