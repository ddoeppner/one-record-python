class ONERecordClientException(Exception):
    """Raised when an error occurs in the request."""

    def __init__(self, message, code=None):
        if isinstance(message, bytes):
            message = message.decode("UTF-8", "replace")

        if code is not None:
            message = f"{code}: {message}"

        super().__init__(message)
        self.message = message
        self.code = code
